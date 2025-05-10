import subprocess

MOD_VERSION = "1.0.2"
VERSION_DATA = [
    {
        "minecraft_version": "1.21.5",
        "loader_version": "0.16.14",
        "yarn_mappings": "1.21.5+build.1",
        "fabric_version": "0.123.2+1.21.5",
    },
    {
        "minecraft_version": "1.21.4",
        "loader_version": "0.16.14",
        "yarn_mappings": "1.21.4+build.8",
        "fabric_version": "0.119.2+1.21.4",
    },
    {
        "minecraft_version": "1.21.3",
        "loader_version": "0.16.14",
        "yarn_mappings": "1.21.3+build.2",
        "fabric_version": "0.114.0+1.21.3",
    },
    {
        "minecraft_version": "1.21.2",
        "loader_version": "0.16.14",
        "yarn_mappings": "1.21.2+build.1",
        "fabric_version": "0.106.1+1.21.2",
    },
    {
        "minecraft_version": "1.21.1",
        "loader_version": "0.16.14",
        "yarn_mappings": "1.21.1+build.3",
        "fabric_version": "0.116.0+1.21.1",
    },
]

if __name__ == "__main__":
    failed_build = []
    failed_upload = []

    for entry in VERSION_DATA[::-1]:
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
mod_version={MOD_VERSION}
maven_group=nodeathanimations.nodeathanimations
archives_base_name=nodeathanimations

# Dependencies
fabric_version={fabric_version}'''
            )

        print(f"=== Building {minecraft_version} ===")
        build_result = subprocess.run(["./gradlew", "build"])
        print(build_result.stdout)
        if build_result.returncode == 0:
            print(f"=== Uploading {minecraft_version} ===")
            upload_result = subprocess.run(["./gradlew", "modrinth"])
            print(upload_result.stdout)
            if upload_result.returncode != 0:
                print(upload_result.stderr)
                failed_upload.append(minecraft_version)
        else:
            print(build_result.stderr)
            failed_build.append(minecraft_version)

    if len(failed_build) == 0 and len(failed_upload) == 0:
        print(">>> All versions built and uploaded successfully")
    else:
        if len(failed_build) > 0:
            print(f">>> Versions {failed_build} failed builds")
        if len(failed_upload) > 0:
            print(f">>> Versions {failed_upload} failed uploads")
