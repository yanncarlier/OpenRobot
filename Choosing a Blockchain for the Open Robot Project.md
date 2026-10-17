# Choosing a Blockchain for the Open Robot Project

*Prepared October 17, 2026*

The right chain depends mostly on whether your robots belong to one operator or several. This document chooses by layer instead of looking for a single winner.

## Public chains

**Base (Coinbase L2).** The most natural default for robot payments today. x402 was designed around it and USDC is native there, so per-call micropayments are cheap and well supported. OpenMind's FABRIC robot identity network is also built on Base, and Circle partnered with OpenMind in early 2026 so robots can transact in USDC. Weaker point: it is a general-purpose chain, so you build the robot permission and identity logic yourself.

**Arc (Circle).** Its mainnet launched on September 16, 2026. It uses USDC for gas, offers sub-second finality, and is EVM-compatible. Predictable fees in a stable currency suit robots that have to budget. Caveats: it uses permissioned proof-of-authority consensus, and Circle is exploring a move to proof of stake in 2027. It is very new, so treat it as promising rather than proven.

**peaq.** The most robot-specific option. It is a Layer-1 for the machine economy, with machine identities (peaq IDs), on-chain wallets, and access control. That matches the permissions and wallets requirements closely, and it is EVM-compatible. Caveats: a smaller ecosystem and less stablecoin liquidity than Base, so check USDC availability. Much of the coverage of robot blockchains comes from crypto media and exchange blogs, so treat the claims with some skepticism.

**Ethereum mainnet.** Too slow and expensive to use directly. It is useful as a periodic anchor for audit hashes if you want maximum neutrality.

## Private / permissioned chains

**Hyperledger Besu (QBFT).** The pick for a consortium. It is EVM-based, so the same smart contracts work on public chains, it has built-in permissioning, and it gives fast, deterministic finality. Choosing the EVM also keeps your options open.

**Hyperledger Fabric.** Strong for private data between organizations, but it has no native payments or wallets, a heavier operational model, and a non-EVM toolchain. It fits an audit-focused consortium better than a wallet-per-robot design.

**Cosmos SDK / CometBFT app-chain.** Good if you want a custom chain with its own rules. It has instant finality and strong light-client support, which matters since robots will not run full nodes. The cost is that you build and operate more yourself.

## What matters for this design

1. **Light-client friendliness.** Robots will verify headers and proofs instead of running full nodes, so check that the chain supports this well.
2. **Deterministic finality.** BFT-style chains (Besu QBFT, CometBFT, Arc) give clear "done" signals, which suit permission changes and payments. Their trade-off is stalling if a quorum cannot be reached, which is acceptable for the slow layer.
3. **Stable, tiny fees.** USDC gas on Arc, or cheap L2 fees on Base, beats volatile token fees for autonomous spending.
4. **EVM compatibility.** It lets you move identity, permission, and payment contracts between chains without a rewrite.

## Recommendation

| Situation | Suggested approach |
| --- | --- |
| Multiple untrusting owners, open ecosystem | Base or Arc for USDC settlement, with identity and permissions in an EVM registry contract (peaq if you want its machine-ID tooling) |
| Consortium or enterprise | Besu on a private network for identity, permissions, and audit, with payments settled on a public USDC chain |
| Single operator | No blockchain; use the CRDT/gossip layer with signed capability tokens |

Because the contracts are EVM, you can start on a public testnet or a local Besu network and change chains later without redesigning the system.

## Addendum: Tron USDT

Tron USDT is a strong payment rail but a weak fit as the main chain for this project. It works best as an optional settlement option.

### What it does well

- **Deep USDT liquidity.** Tron ended Q2 2026 with about $87.9 billion of circulating USDT, roughly 47.6% of tracked supply and ahead of Ethereum. If your counterparties or customers hold USDT, this is where they are.
- **Fast finality.** Transfers settle in about three seconds, which is fast enough for the slow layer.
- **Agent infrastructure is arriving.** B.AI launched on Tron in April 2026 as a financial layer for AI agents, with ERC-8004 and x402 support.

### Why it is a weak fit here

- **Fees are too high for micropayments.** One fee guide puts a typical TRC-20 USDT transfer at about $1.00 to $3.50 of TRX, and burning TRX for energy costs 6.5 to 13 TRX per transfer unless you rent or stake energy. That works for larger settlements, but per-call payments of a few cents do not fit. Base and Arc are far cheaper for that. These figures come from wallet and energy-rental sites, so check live costs.
- **A second asset to manage.** Fees run on energy and TRX, so every robot needs TRX or rented energy alongside USDT. On Arc, USDC pays the gas directly.
- **USDT is freezable.** Tether can blacklist addresses, so a compromised or flagged robot could have its balance frozen. Check how each issuer handles freezes before depending on it.
- **x402 mostly runs on USDC.** Circle reported that USDC made up 99.3% of x402 payment volume in Q2 2026. As far as I know, USDT also lacks the gasless signed-authorization transfers that x402's standard flow relies on, so Tron support probably needs a different mechanism. Verify this before building on it.
- **Light clients.** As far as I know, Tron has a weaker trust-minimized light-client story than Ethereum-family or Cosmos chains, so robots would likely lean on API providers. This also needs checking.
- **Governance concentration.** Tron uses delegated proof of stake with a small set of block producers. That is acceptable for a distributed, not decentralised, design, but it is a dependency to weigh.

Tron's own quarterly reports are marketing as much as analysis. The supply figures are corroborated by multiple sources, but the agent-economy claims are early.

### How to use it

1. Put identity, permissions, and audit on an EVM chain (Base, Arc, or Besu), as recommended above.
2. Keep USDC on Base or Arc for robot-to-robot micropayments.
3. Add Tron USDT only as an optional settlement adapter for cases where a counterparty requires USDT. Aggregate many small payments in payment channels or signed vouchers first, then settle in one larger TRC-20 transfer to cut the fee overhead.
