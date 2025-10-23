import ipaddress

def subnet_calculator():
    print("== Subnet Calculator ==")
    
    # Ask for input
    ip_input = input("Enter an IP address (e.g., 192.168.1.0/24): ")
    
    try:
        network = ipaddress.IPv4Network(ip_input, strict=False)

        print(f"\nNetwork Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"Number of Usable Hosts: {network.num_addresses - 2}")
        print(f"First Host: {list(network.hosts())[0]}")
        print(f"Last Host: {list(network.hosts())[-1]}")
        
    except ValueError :
        print("Invalid input. Please use correct format (e.g., 192.168.1.0/24)")

# Main
subnet_calculator()

# Challenge 1: Plan Quotas
variable "user_plan" {
  description = "Selected subscription plan"
  default     = "pro"
}

locals {
  plan_quotas = {
    free       = 100
    pro        = 1000
    enterprise = 10000
  }
}

# Challenge 2: Region Endpoints
variable "region" {
  description = "Selected deployment region"
  default     = "eu-west-1"
}

locals {
  region_endpoints = {
    "us-east-1" = "api.use1.example.com"
    "eu-west-1" = "api.euw1.example.com"
  }

  override_endpoints = {
    "ap-south-1" = "api.aps1.example.com"
  }
}

# Challenge 3: Nested Greetings
variable "lang" {
  description = "Language code for greetings"
  default     = "fr"
}

locals {
  greetings = {
    en = { hello = "Hello" }
    fr = { hello = "Bonjour" }
    es = { hello = "Hola" }
  }
}

# Challenge 4: City Airport Codes
variable "requested_cities" {
  description = "Cities to resolve to airport codes"
  type        = list(string)
  default     = ["Toronto", "Ottawa", "Vancouver"]
}

locals {
  city_codes = {
    Toronto   = "YYZ"
    Vancouver = "YVR"
    Montreal  = "YUL"
  }
}

# Challenge 5: Environment Presence
variable "environment" {
  description = "Environment to test presence in env_settings"
  default     = "stage"
}

locals {
  sentinel_missing = "MISSING"

  env_settings = {
    dev  = "t2.micro"
    qa   = "t3.small"
    prod = "m5.large"
  }
}

# Challenge 6: Service Ports
variable "service" {
  description = "Service to fetch port for"
  default     = "api"
}

locals {
  base_ports = {
    web = 80
    api = 8080
  }

  custom_ports = {
    api = 9000
  }
}

# Challenge 7: Country Code Case-Insensitive Lookup
variable "country_input" {
  description = "Country name for code lookup (case-insensitive demo)"
  default     = "usa"
}

locals {
  country_codes_mixed = {
    Canada = "CA"
    USA    = "US"
    Mexico = "MX"
  }

  normalized_country_codes = { for k, v in local.country_codes_mixed : lower(k) => v }
}

# Challenge 8: Product Price Fallbacks
variable "product" {
  description = "Which product to price"
  default     = "widget"
}

locals {
  regional_prices = {
    "eu-west-1" = {
      widget = 12.5
      pro    = 49.9
    }
    "us-east-1" = {
      widget = 10.0
    }
  }

  global_prices = {
    widget = 15.0
    pro    = 59.0
  }
}

# Challenge 9: Feature Flags
variable "feature_to_check" {
  description = "Which feature flag to read"
  default     = "chat"
}

locals {
  feature_flags = {
    chat   = true
    search = false
  }
}
