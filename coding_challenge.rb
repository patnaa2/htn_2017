# Coding Challenge:
# Print Fizz if number is divisible by 3
# Print Buzz if number is divisible by 5


def fizzbuzz(num)
puts "fizz" if num%3 ==0

puts "buzz" if num % 5 ==0
end


16.times do |n|
  fizzbuzz(n)
end
