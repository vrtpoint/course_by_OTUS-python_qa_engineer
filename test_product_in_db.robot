*** Settings ***
Documentation   Suite description
Library          Selenium2Library
Library DatabaseLibrary

Connect To Database pymysql   ${DBname}    ${DBuser}    ${DBHost}    ${DBPort}


*** Variables ***
${URL}                      http://localhost/admin
${BROWSER}                  Firefox
${USERNAME_FIELD}           id:input-username
${PASSWORD_FIELD}           id:input-password
${USER}                     user
${PASSWORD}                 bitnami1
${LOGIN_BUTTUN}             css:button[type='submit']
${CATALOG}                  css:li[id='menu-catalog']
${PRODUCTS}                 xpath=*//a[text()='Products']
${LOGOUT_BUTTUN}            xpath=//*[@id="header"]/div/ul/li[2]/a/span
${ADD_NEW_BUTTON}           xpath=//*[@id="content"]/div[1]/div/div/a/i
${PRODUCT_NAME_FIELD}       xpath=//*[@id="input-name1"]
${META_TAG_TITLE_FIELD}     xpath=//*[@id="input-meta-title1"]
${NAVIGATION_DATA}          xpath=//*[@id="form-product"]/ul/li[2]/a
${MODEL_FIELD}              xpath=//*[@id="input-model"]
${SAVE_BUTTON}              xpath=//*[@id="content"]/div[1]/div/div/button
${NEW_PRODUCT}              iPhone 11 Pro Max 64 GB
${EDIT_PRODUCT}             iPhone 11 Pro Max 256 GB
${TAG}                      iOS 13
${NEW_MODEL}                A2215
${EDIT_MODEL}               A2218
${PRODUCT_TO_DELETE}        xpath=//*[@id="form-product"]/div/table/tbody/tr[1]/td[1]/input
${DELETE_BUTTON}            xpath=//*[@id="content"]/div[1]/div/div/button[3]
${DBname}   bitnami_opencart
${DBuser}   bn_opencart
${DBHost}   localhost
${DBPort}   3306


*** Test Cases ***
Add new product
    Open browser                        ${URL}  ${BROWSER}
    Maximize Browser Window
    Input text                          ${USERNAME_FIELD}    ${USER}
    Input text                          ${PASSWORD_FIELD}    ${PASSWORD}
    Click Button                        ${LOGIN_BUTTUN}
    Click Element                       ${CATALOG}
    Wait Until Element Is Visible       ${PRODUCTS}
    Click Element                       ${PRODUCTS}
    Wait Until Element Is Visible       ${ADD_NEW_BUTTON}
    Click Element                       ${ADD_NEW_BUTTON}
    Click Element                       ${PRODUCT_NAME_FIELD}
    Input text                          ${PRODUCT_NAME_FIELD}    ${NEW_PRODUCT}
    Click Element                       ${META_TAG_TITLE_FIELD}
    Input text                          ${META_TAG_TITLE_FIELD}    ${TAG}
    Click Element                       ${NAVIGATION_DATA}
    Wait Until Element Is Visible       ${MODEL_FIELD}
    Click Element                       ${MODEL_FIELD}
    Input text                          ${MODEL_FIELD}    ${NEW_MODEL}
    Click Button                        ${SAVE_BUTTON}
    Wait Until Element Is Not Visible   ${SAVE_BUTTON}
    Check If Exists In Database select * from oc_product where model="test"
    Close browser


Delete product
    Open browser                        ${URL}  ${BROWSER}
    Maximize Browser Window
    Input text                          ${USERNAME_FIELD}    ${USER}
    Input text                          ${PASSWORD_FIELD}    ${PASSWORD}
    Click Button                        ${LOGIN_BUTTUN}
    Click Element                       ${CATALOG}
    Wait Until Element Is Visible       ${PRODUCTS}
    Click Element                       ${PRODUCTS}
    Click Element                       ${PRODUCT_TO_DELETE}
    Wait Until Element Is Visible       ${DELETE_BUTTON}
    Click Button                        ${DELETE_BUTTON}
    Handle Alert
    Check If No Exists In Database select * from oc_product where model="test"
    Close browser
