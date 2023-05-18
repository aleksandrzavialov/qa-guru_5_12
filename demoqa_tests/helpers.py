from selene import be, command
from selene.support.shared import browser


def remove(selector):
    if browser.element(selector).wait_until(be.visible):
        browser.element(selector).perform(command.js.remove)