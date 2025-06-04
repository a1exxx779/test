resource "azurerm_resource_group" "claudiu" {
  name     = "Alex-juneploy-test"
  location = "West Europe"
  tags = {
    owner = "silviu.stroe@redbull.com"
  }
}
