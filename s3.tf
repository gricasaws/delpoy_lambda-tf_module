resource "aws_s3_bucket" "example" {
    bucket = "test-gricas-show-useful-lambda"
    acl = "private"
}