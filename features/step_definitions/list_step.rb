Given(/^the input "([^"]*)" "([^"]*)"$/) do |arg1, arg2|
  @input=arg1,@input2=arg2
end

When(/^the program is run$/) do
  @output = `python list.py #{@input} #{@input2}`
  raise('Command Failed!') unless $?.success?
end

Then(/^the output should be "([^"]*)"$/) do |arg1|
  expect(@output).to eq(arg1)
end

