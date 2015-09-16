Given(/^the input "([^"]*)"$/) do |arg1|
  @input=arg1
end

When(/^the program is run with no file$/) do
  @output = `/usr/bin/python list.py #{@input}`
  raise('Command Failed!') unless $?.success?
end

Then(/^the output now should be "([^"]*)"$/) do |arg1|
  expect(@output).to eq(arg1)
end