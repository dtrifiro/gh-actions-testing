variable "GITHUB_SHA" {}
variable "GITHUB_REPO" {}
variable "GITHUB_RUN_ID" {}

group "default" {
  targets = [
    "mytarget",
  ]
}

target "mytarget" {
  dockerfile = "Dockerfile"

  args = {
  }
  labels = {
    "org.opencontainers.image.source" = "https://github.com/${GITHUB_REPO}"
    "vcs-ref" = "${GITHUB_SHA}"
    "vcs-type" = "git"
  }
  tags = [
    "${REPOSITORY}:${GITHUB_SHA}",
    "${REPOSITORY}:${formatdate("YYYY-MM-DD-hh-mm", timestamp())}"
  ]
}
