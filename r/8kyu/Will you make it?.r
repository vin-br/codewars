# Loading packages
library(testthat)

# Function to check if you can reach the pump with the remaining fuel
zero_fuel <- function(distance_to_pump, mpg, fuel_left) {
  ifelse(mpg * fuel_left >= distance_to_pump, TRUE, FALSE)
}

# Tests with testthat library
test_that('basic tests', {
  expect_equal(zero_fuel(50, 25, 2), TRUE)
  expect_equal(zero_fuel(60, 30, 3), TRUE)
  expect_equal(zero_fuel(70, 25, 1), FALSE)
  expect_equal(zero_fuel(100, 25, 3), FALSE)
})
