variable "bucket_name" { 
    type = string 
}

variable "tags" { 
    type = map(string) 
    default = {} 
}

variable "protect" {
    type = bool
    default = false 
} 

variable "purpose" {
    type = string
}

variable "block_public_access"  { 
    type = bool 
    default = true 
}
variable "versioning" { 
    type = bool 
    default = true 
}

variable "sse_algorithm"  { 
    type = string
    default = "AES256" 
} 