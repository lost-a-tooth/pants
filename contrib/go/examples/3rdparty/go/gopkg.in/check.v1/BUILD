# Auto-generated by pants!
# To re-generate run: `pants buildgen.go --materialize --remote`

go_remote_library(
  # NB: We pin this rev for 2 reasons:
  # 1. It turns out v1 is backed by a branch and not a tag so despite the gopkg.in version pinning,
  #    The v1 branch can float.
  # 2. Without a pin, integration tests hit the github API to resolve the latest compatible v1
  #    tag/branch and this runs into rate-limit issues quickly on Travis CI.
  rev='9217c9979615bf07fc41eb86b91e334b093ff20d'
)
