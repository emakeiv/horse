locals {
  merged_tags = var.purpose != "" ? merge(var.tags, { Purpose = var.purpose }) : var.tags
}