MOD_VERSION = "1.0.2"
VERSION_DATA = [
    {
        "minecraft_version": "1.20.4",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.20.4+build.3",
        "fabric_version": "0.91.3+1.20.4",
    },
    {
        "minecraft_version": "1.20.3",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.20.3+build.1",
        "fabric_version": "0.91.1+1.20.3",
    },
    {
        "minecraft_version": "1.20.2",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.20.2+build.4",
        "fabric_version": "0.91.2+1.20.2",
    },
    {
        "minecraft_version": "1.20.1",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.20.1+build.10",
        "fabric_version": "0.91.0+1.20.1",
    },
    {
        "minecraft_version": "1.20",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.20+build.1",
        "fabric_version": "0.83.0+1.20",
    },
    {
        "minecraft_version": "1.19.4",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.19.4+build.2",
        "fabric_version": "0.87.2+1.19.4",
    },
    {
        "minecraft_version": "1.19.3",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.19.3+build.5",
        "fabric_version": "0.76.1+1.19.3",
    },
    {
        "minecraft_version": "1.19.2",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.19.2+build.28",
        "fabric_version": "0.77.0+1.19.2",
    },
    {
        "minecraft_version": "1.19.1",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.19.1+build.6",
        "fabric_version": "0.58.5+1.19.1",
    },
    {
        "minecraft_version": "1.19",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.19+build.4",
        "fabric_version": "0.58.0+1.19",
    },
    {
        "minecraft_version": "1.18.2",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.18.2+build.4",
        "fabric_version": "0.77.0+1.18.2",
    },
    {
        "minecraft_version": "1.18.1",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.18.1+build.22",
        "fabric_version": "0.46.6+1.18",
    },
    {
        "minecraft_version": "1.18",
        "loader_version": "0.15.0",
        "yarn_mappings": "1.18+build.1",
        "fabric_version": "0.46.6+1.18",
    },
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