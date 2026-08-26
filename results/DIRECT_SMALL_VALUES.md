# Direct Small Values

Date: 2026-08-25

## Provenance

- Solver model: direct total-domination MILP, one binary variable per vertex, one open-neighborhood domination constraint per vertex.
- Solver independence: no automaton imports or automaton state/transition code.
- CBC executable: bundled CBC solver (version 2.10.3)
- CBC version command: `cbc -stop`
- CBC version output:

```text
Welcome to the CBC MILP Solver
Version: 2.10.3
Build Date: Dec 15 2019

command line - cbc -stop (default strategy 1)
Total time (CPU seconds):       0.00   (Wallclock seconds):       0.00
```

## Reproduction

Run from the repository root:

```text
pytest tests/test_direct.py tests/test_small_values.py -q
```

Witness serialization for `witness_sha256`: sorted selected vertices as ASCII lines `row,column\n`.

Model hash: SHA-256 of the LP text emitted by `src.direct.milp_probe._write_lp` for that `(m,n)`.

## Records

| m | n | value | witness_sha256 | model_sha256 |
|---:|---:|---:|---|---|
| 5 | 3 | 5 | `7744744f9beb0c433a8a8c4ef5e095c152b161f00e709bef2915d99152bd00db` | `fbcd398dbeab9ff72c0da56641645831b86035ac204f7dc710eecbe411367adf` |
| 5 | 6 | 10 | `bb92fe40a90e18b6d4ef24b5d61a8289ae07afd144419863bdc8a54b476a7e09` | `6ff148b616768acae53aa2123225169a322008c7da6f434b1c033979ffa4e18f` |
| 5 | 10 | 16 | `fc73e07a99e09a6324bb2abc22599a2eccfb15004ecad6e7457fd3540595e592` | `f5c00c8f04007898dc6e2ca9b7647430310acd0597f072634ffd92616006841b` |
| 5 | 14 | 22 | `1b25b33f68ba23370ebaf613717cbb026ee535b0a88bbd5c20f861e1bc4c8b48` | `e4f657f3cded5e30be37e42f04d56d459bf01d0caa62a9efaede7d36ad63eddf` |
| 5 | 20 | 30 | `9af979e2d756b9d871b784b322b0b6d984019195335a9dda7a0dc6c368a10b4a` | `b4fe959f96f4f7d997ced78eac3b2c74dbbd58ad162a94a4c5210e7db32875b9` |
| 6 | 3 | 6 | `fce3c0de1e659e46c58b63c47d8f8bbafb3cd467ea44dbe463bacd8580342d4d` | `18162489c9afbfb92163736b1be119501ef0d7e0422d1088ecebaf6cfffd8dc1` |
| 6 | 4 | 8 | `3027f36e808688d6da77bf1e933af51dba0f27d07c01d953cb8d82b7c02b9674` | `607f0a7b4e88d9c2038a984b26b56b1aa5c6d4df9a9a5899111b61c21eb20664` |
| 6 | 8 | 16 | `dfb37de9af6b15b285fc04345c1e04dce450e3abc2a190c9faf65c8594b63a6f` | `7d95a80e8e36c5f52bb76150a9fd83937367d873ae23fe91332e8eef36ebc1c6` |
| 6 | 12 | 22 | `0c0e2836b42be1f871ce92a0c36f0fe14ecf2cac40262e68a0efad5ff278ecbf` | `da328442d9d102c757c77915157ca1cd368448834aa98e4154b885536e7b4942` |
| 6 | 14 | 24 | `08db6ab29b8662e8d3412ddd45c8dc3c2935dbd1d60da837c1a1e26a8dfef409` | `1d2339b41739c2a2c86835f921572097a95035de781229d15331d8f28447277e` |
| 6 | 21 | 36 | `d57bef023b26b011446e562724de7267828884d6f40f9e89a840df50e0accbcc` | `a236f37aa6ffa18d15ca519e1bfbde79e6395115da7074740a56e1c57903c46d` |
| 6 | 26 | 48 | `3bd0ddb428d79a095536c9c8eab16f9d6be484b9c0edd4929feec3d07247f6ef` | `c476b37cc34ac0b4e7899c327e5d3d5206602e28fd8924b4913f31c6f782057a` |
| 7 | 3 | 6 | `107c4f098706f7eec28a98d583b147b4db1747fd67d0654eb1ea959de60aadaa` | `aa74c77d70ad366016a97f294f098a53ccd213ed6b4f69f369c1498a41f812a2` |
| 7 | 7 | 15 | `138de5c44e4b405e8bc29620d0064d298af967ba2cbe9c58191d915931341bb3` | `7e68b105c2f807aa6ecb5ed289c62e008ac18e5b70a628b5c3ea16925ca461a8` |
| 7 | 14 | 30 | `c7f47bf27a8a5750d3adfdf914278e371091d253ebbcce561d3bac1252da04fc` | `4e8cc075625074c03a4fe1f75bca4015b95a4e5d512179ec6fe86ff223a8f829` |
| 7 | 15 | 30 | `e19f8046c07093ceb485071f29985af64b6ad4ee3e14d02c78bc7fe3afb39a64` | `fc740f48c2d4c6ebb569b8cdeea753099983c9faece730e49a851f9386d1aac3` |
| 7 | 20 | 40 | `b76bd42184c97e51491e62c47b9b15fc1da42580af0a4949cff132dd867b4211` | `d13fb0c5f8c9500773cf41f96c737cc249f73a6fc7dd5bb79e6a4f280aad8b9f` |
