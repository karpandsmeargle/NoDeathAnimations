MOD_VERSION = "1.0.2"
VERSION_DATA = [
    {
        "minecraft_version": "1.20.4",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.20.4+build.3",
        "fabric_version": "0.91.3+1.20.4",
    }
]

for entry in VERSION_DATA:
    minecraft_version = entry["minecraft_version"]
    loader_version = entry["loader_version"]
    yarn_mappings = entry["yarn_mappings"]
    fabric_version = entry["fabric_version"]
    with open("gradle.properties", "w") as fout:
        fout.write(
            f'''\
# Done to increase the memory available to gradle.
org.gradle.jvmargs=-Xmx1G
org.gradle.parallel=true

# Fabric Properties
# check these on https://fabricmc.net/develop
minecraft_version={minecraft_version}
yarn_mappings={yarn_mappings}
loader_version={loader_version}

# Mod Properties
mod_version=1.0.2
maven_group=nodeathanimations.nodeathanimations
archives_base_name=nodeathanimations

# Dependencies
fabric_version={fabric_version}'''
        )