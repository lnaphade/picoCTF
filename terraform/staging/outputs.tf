
output "Staging Web Elastic IP address" {
    value = "${aws_eip.web.public_ip}"
}

output "Staging Shell Elastic IP address" {
    value = "${aws_eip.shell.public_ip}"
}

output "Staging DB Elastic IP address" {
    value = "${aws_eip.db.public_ip}"
}
