This library was built for [coherent.build](https://github.com/coherent-oss/coherent.build) and [skeleton](https://blog.jaraco.com/skeleton) projects to inject a license file at build time to reflect the license declared in the License Expression.

## Setuptools Plugin

### Installation

This plugin is intended only to be installed as a build requirement. Avoid installing it except temporarily for a build that requires it. If it is installed to a shared/system environment, it will be activated for all Setuptools builds and emit a warning. If the target ecosystem expects build artifacts to be installed to a shared environment, the warning can be disabled by setting `COHERENT_LICENSED_UNUSED_ACTION=ignore`.
