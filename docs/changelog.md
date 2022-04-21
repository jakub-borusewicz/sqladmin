# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Version 0.1.8 - 2022-04-19

### Added

* Add csv export support in [#101](https://github.com/aminalaee/sqladmin/pull/101)
* Expose Starlette middlewares and debug to the Admin in [#114](https://github.com/aminalaee/sqladmin/pull/114)

### Fixed

* Fix Export unlimited rows in [#107](https://github.com/aminalaee/sqladmin/pull/107)
* Add form and export options docs in [#110](https://github.com/aminalaee/sqladmin/pull/110)
* fix docstring issues by adding an explicit handler in [#106](https://github.com/aminalaee/sqladmin/pull/106)
* Fix get_model_attr with column labels in [#128](https://github.com/aminalaee/sqladmin/pull/128)
* Delay call to `self.get_converter` to use `form_overrides` in [#129](https://github.com/aminalaee/sqladmin/pull/129)

**Full Changelog**: https://github.com/aminalaee/sqladmin/compare/0.1.7...0.1.8

## Version 0.1.7 - 2022-03-22

### Added

* Add SQLModel support in [#94](https://github.com/aminalaee/sqladmin/pull/94)
* Add form-specific functionality to ModelAdmin in [#97](https://github.com/aminalaee/sqladmin/pull/97)
* Add `UUID` field converter in [#82](https://github.com/aminalaee/sqladmin/pull/82)
* Add PostgreSQL `INET` and `MACADDR` converters in [#83](https://github.com/aminalaee/sqladmin/pull/83)

### Fixed

* Fix Boolean field checkbox UI in [#88](https://github.com/aminalaee/sqladmin/pull/88)
* Fix PostgreSQL UUID PrimaryKey in [#92](https://github.com/aminalaee/sqladmin/pull/92)
* Fix Source Code Link in [#95](https://github.com/aminalaee/sqladmin/pull/95)

**Full Changelog**: https://github.com/aminalaee/sqladmin/compare/0.1.6...0.1.7

## Version 0.1.6 - 2022-03-09

### Added

* FontAwesome6 icons in [#78](https://github.com/aminalaee/sqladmin/pull/78)
* Add `column_sortable_list` in [#65](https://github.com/aminalaee/sqladmin/pull/65)
* Add JSON column converters in [#74](https://github.com/aminalaee/sqladmin/pull/74)

### Fixed

* Fix URL search regex in [#67](https://github.com/aminalaee/sqladmin/pull/67)
* Fix Enum in Edit page in [#71](https://github.com/aminalaee/sqladmin/pull/71)

**Full Changelog**: https://github.com/aminalaee/sqladmin/compare/0.1.5...0.1.6

## Version 0.1.5 - 2022-02-24

### Added

* Authentication in [#37](https://github.com/aminalaee/sqladmin/pull/37)
* Add Edit view page in [#60](https://github.com/aminalaee/sqladmin/pull/60)
* Add `column_searchable_list` in [#61](https://github.com/aminalaee/sqladmin/pull/61)

### Internal

* Cleanup DB queries in [#51](https://github.com/aminalaee/sqladmin/pull/54)

**Full Changelog**: https://github.com/aminalaee/sqladmin/compare/0.1.4...0.1.5

## Version 0.1.4 - 2022-02-16

### Added

* Allow templates to be configured in [#52](https://github.com/aminalaee/sqladmin/pull/52)
* Add page size option links in [#34](https://github.com/aminalaee/sqladmin/pull/34)

### Fixed

* Improve pagination in [#36](https://github.com/aminalaee/sqladmin/pull/36)

### Internal

* Instantiate ModelAdmin internally to avoid class methods in [#31](https://github.com/aminalaee/sqladmin/pull/31)

**Full Changelog**: https://github.com/aminalaee/sqladmin/compare/0.1.3...0.1.4

## Version 0.1.3 - 2022-01-24

### Added

* Add `title` and `logo` options in [#20](https://github.com/aminalaee/sqladmin/pull/20)
* Adding `order_by` to list pagination query in [#25](https://github.com/aminalaee/sqladmin/pull/25)
* Allow Relationship properties in list and detail views in [#22](https://github.com/aminalaee/sqladmin/pull/22)

**Full Changelog**: https://github.com/aminalaee/sqladmin/compare/0.1.2...0.1.3