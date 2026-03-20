# Changelog

## [1.3.0](https://github.com/jbussdieker/bussdcc-config/compare/v1.2.0...v1.3.0) (2026-03-20)


### Features

* **config:** restructure schema handling and update dependencies ([0e9be8d](https://github.com/jbussdieker/bussdcc-config/commit/0e9be8d926709b7a477e8b913df69995979e97a1))

## [1.2.0](https://github.com/jbussdieker/bussdcc-config/compare/v1.1.0...v1.2.0) (2026-03-17)


### Features

* **config:** handle optional types in schema field processing ([c1e8653](https://github.com/jbussdieker/bussdcc-config/commit/c1e8653f7b4be7b4c884c1d9272dbe12087f2ecd))

## [1.1.0](https://github.com/jbussdieker/bussdcc-config/compare/v1.0.0...v1.1.0) (2026-03-17)


### Features

* **deps:** update bussdcc-framework to v0.24.0 ([d198081](https://github.com/jbussdieker/bussdcc-config/commit/d198081012d9a7f1cf4c1468c2b906ab3e0ef98a))

## [1.0.0](https://github.com/jbussdieker/bussdcc-config/compare/v0.4.0...v1.0.0) (2026-03-17)


### ⚠ BREAKING CHANGES

* **config:** build_dataclass is no longer exported from bussdcc_config.config; use bussdcc_framework.util.build_dataclass instead.

### Code Refactoring

* **config:** remove local dataclass builder and support nested container schemas ([1e60243](https://github.com/jbussdieker/bussdcc-config/commit/1e602439ab9d1f886d121f164ec7e87fc5d8cb90))

## [0.4.0](https://github.com/jbussdieker/bussdcc-config/compare/v0.3.0...v0.4.0) (2026-03-16)


### Features

* **config, interface:** enhance type handling and update JSON usage ([0d2291a](https://github.com/jbussdieker/bussdcc-config/commit/0d2291ab70e786e106b3ca2bd4bb53c242062654))

## [0.3.0](https://github.com/jbussdieker/bussdcc-config/compare/v0.2.0...v0.3.0) (2026-03-14)


### Features

* **config, interface:** add new fields and improve form rendering ([518db97](https://github.com/jbussdieker/bussdcc-config/commit/518db97a4b9d19277ff0ec786bcd9deab7ca05c5))

## [0.2.0](https://github.com/jbussdieker/bussdcc-config/compare/v0.1.0...v0.2.0) (2026-03-13)


### Features

* **config, interface:** enhance metadata and form elements ([ce9c90a](https://github.com/jbussdieker/bussdcc-config/commit/ce9c90a62fdfd77cae5ec7651c234cea106c5d6f))
* **config, interface:** enhance schema handling and dataclass building ([6f84cf9](https://github.com/jbussdieker/bussdcc-config/commit/6f84cf9935edbee1d698c167b6e454647598a26b))
* **config, interface:** refactor schema handling and improve form rendering ([d62edf2](https://github.com/jbussdieker/bussdcc-config/commit/d62edf2b367b1f0abe0da09e759701fd7e5b43c7))
* **config:** enforce required fields in metadata ([a10a9f0](https://github.com/jbussdieker/bussdcc-config/commit/a10a9f047c238bffa038039c0aa50288e0e1b367))
* **config:** introduce FieldMeta for enhanced schema metadata handling ([9437df5](https://github.com/jbussdieker/bussdcc-config/commit/9437df5fae5856c146154abc5e4841ef9c2a1b29))
* **interface:** display config name on home page ([85e0445](https://github.com/jbussdieker/bussdcc-config/commit/85e0445077eb7551a41b095c16070a62749699ef))
* **interface:** enhance configuration management ([f777ed4](https://github.com/jbussdieker/bussdcc-config/commit/f777ed45c47708ce54650909f107128605931326))
* **interface:** enhance form field attribute handling ([a4abcda](https://github.com/jbussdieker/bussdcc-config/commit/a4abcda1f9a067798993fc8fed9079680959b654))
* **interface:** improve form element accessibility ([5b2d185](https://github.com/jbussdieker/bussdcc-config/commit/5b2d18560010647da07702bced3e4209631cf397))
* **interface:** improve form structure and field handling ([263d237](https://github.com/jbussdieker/bussdcc-config/commit/263d2373677151df174b17b52809f6f62a33447f))
* **interface:** update UI to reflect config changes in real-time ([2ff5e28](https://github.com/jbussdieker/bussdcc-config/commit/2ff5e2845c67ec1b422599b55446392af703bbe9))


### Bug Fixes

* **config, interface:** improve handling of empty configurations ([f0d60b1](https://github.com/jbussdieker/bussdcc-config/commit/f0d60b1c375d34fcde70c10ea89aba519baaa03f))
* **config:** handle empty config data gracefully ([58510d5](https://github.com/jbussdieker/bussdcc-config/commit/58510d5209d79f09475cd0fb3ce67abfcf4c241a))
* **config:** prevent saving when config is empty ([ed90a99](https://github.com/jbussdieker/bussdcc-config/commit/ed90a992dfd88d0997490655d908e4b2ab77bc22))
* **config:** update type annotation for SchemaField ([97fabd9](https://github.com/jbussdieker/bussdcc-config/commit/97fabd9a46aa0b0ed82a3d3ce25cf6d891e91eef))
* **interface:** conditionally render help text in form template ([8ca02c8](https://github.com/jbussdieker/bussdcc-config/commit/8ca02c8415d540995db25e38af22dabafccf52a8))
* **interface:** correct condition check for configuration initialization ([dc19014](https://github.com/jbussdieker/bussdcc-config/commit/dc1901435daeedd82299e6d2f91081f712260a21))

## 0.1.0 (2026-03-12)


### Features

* initial commit ([dba9041](https://github.com/jbussdieker/bussdcc-config/commit/dba9041afadb884aa72ae36633470fe2fa482a7b))
