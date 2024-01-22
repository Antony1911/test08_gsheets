import gspread
from oauth2client.service_account import ServiceAccountCredentials
import binascii
from Crypto.Cipher import AES
import getpass
import PySimpleGUI as sg
from tkinter import *
from tkinter import filedialog
import json
import ctypes
import keyboard
import threading
sg.theme('SystemDefault1')
keyMain = '5a677564567332496852716157716a376f774d774e5763314d766b6a36477548'



# ----------------------------------------------------
# Tablet
# ----------------------------------------------------
def get_correct_name_list(name_list):
    corrected_list = []
    for sub_list in name_list:
        sub_list_index = name_list.index(sub_list)
        
        temp_list = []
        for sub in sub_list:
            sub_index = sub_list.index(sub)
            
            count_void = sub_list.count('')
            num = 0
            
            if sub == '':
                try:
                    while count_void != num:
                        sub = corrected_list[sub_list_index - 1][sub_index + num]
                        if sub not in temp_list:
                            temp_list.append(sub)
                        num = num + 1
                except:
                    pass
            else:
                temp_list.append(sub)
                
        corrected_list.append(temp_list)
    return corrected_list
def get_checklist_for_partner():
        
    row_list = ['Name', 'CMS key', 'Основа', f'{partner_name}']
    col_list = []
    
    get_name_col = sheet.get('B:F')
    name_col = get_correct_name_list(get_name_col)
    
    key_col = sheet.col_values(11)
    main_col = sheet.col_values(13)
    indx = partners.index(partner_name)
    partner_col = sheet.col_values(13 + indx)
    
    for i in range(0, 435):
        temp_list_add_to_col_list = []
        temp_list_add_to_col_list.append(name_col[i])
        temp_list_add_to_col_list.append(key_col[i])
        temp_list_add_to_col_list.append(main_col[i])
        temp_list_add_to_col_list.append(partner_col[i])
        
        col_list.append(temp_list_add_to_col_list)
    # print(col_list)
    # https://docs.google.com/spreadsheets/d/1Ebof_JtrKXJiUmCKPnP_tbWAtfGjA-cINeQXhbxkuzQ/edit#gid=1628117538
    return row_list, col_list
def create_partner_list():
    temp_list = sheet.row_values(1)
    except_list = ['','Функционал на сайте', 'Базовый', 'Android', 'iOS', 'Ключ в CMS', 'Настраивается']
    partners = []
    for i in temp_list:
        if i not in partners:
            if i not in except_list:
                partners.append(i)
    return partners
def get_partner_names():
        layout = [
            [sg.Text(f"Choose partner (available = {len(partners)})")],
            [sg.Input(size=40, key='SEARCH', enable_events=True)],
            [sg.Listbox(partners, size=(40, 15), select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, key='LISTBOX')],
            [sg.Text('Remote Config')],
            [sg.Input('', key='HEX')],
            [sg.Button('Submit')],
            # [sg.Button('Submit'), sg.Button(sg.SYMBOL_DOWN, key='EXPAND')],
        ]
        window = sg.Window('choose partner', layout, finalize=True)
        # window['SEARCH'].bind("<Return>", "+RETURN")
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            search = values['SEARCH']
            if values['SEARCH'] != '':
                new_values = [x for x in partners if search.title() in x]
                window.Element('LISTBOX').Update(new_values)
            else:
                window.Element('LISTBOX').Update(partners)
            
            if event == 'Submit':
                selected = values['LISTBOX']
                try:
                    data = json.loads(values['HEX'])
                    ivMain = data['data']['ivHex']
                    decodeConfig(data['data']['dataHex'], keyMain, ivMain)
                except:
                    pass
                return selected
        window.close()
def show_tablet():
    row_list, col_list = get_checklist_for_partner()
    layout = [
        [sg.Table(
            values = col_list, headings=row_list,
            auto_size_columns = 1,
            vertical_scroll_only = 0,
            justification = 'center',
            num_rows = 30,
            key = 'tablet',
            selected_row_colors=('yellow', None),
            alternating_row_color=('#383734'),
            # font="Consolas"
            font=(None, 15),
            enable_events=True,
            expand_x=True,
            expand_y=True,
            enable_click_events=True,
            # display_row_numbers = 1
            
            )
        ]
    ]

    window = sg.Window('test_tablet title', layout, resizable=1)
    
    while True:
        event, value = window.read()
        try:
            window.TKroot.title(col_list[value['tablet']])
        except(TypeError):
            pass
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if '+CLICKED+' in event:
            try:
                window.TKroot.title(col_list[value['tablet']])
            except(TypeError):
                pass
            # pyperclip.copy(event['tablet'])
            print('12345978')
    window.close()
# ----------------------------------------------------
# Hex
# ----------------------------------------------------
def check_language():
    if hex(ctypes.WinDLL('user32', use_last_error=True).GetKeyboardLayout(ctypes.WinDLL('user32', use_last_error=True).GetWindowThreadProcessId(ctypes.WinDLL('user32', use_last_error=True).GetForegroundWindow(), 0)) & (2**16 - 1)) == "0x409":
        print('eng_local')
    else:
        keyboard.press_and_release('win+space')
def readDictPath(path):
    with open(path, "r", encoding='utf-8') as f:
        content = f.read()
    return content
def decodeConfig(hex_bytes, key,  ivStr):
    # hex_bytes = readDictPath(path)
    # for elem in [hex_bytes[i:i+31] for i in range(0, len(hex_bytes), 31)]:
    #     print(elem)
    
    # конвертация hexadecimal-байтов в байты
    bytes = binascii.unhexlify(hex_bytes)

    # конвертация ключа в байты
    key = binascii.unhexlify(key)

    # конвертация IV в байты
    iv = binascii.unhexlify(ivStr)

    # создание объекта AES cipher с mode-CBC
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # декодирование байтов с помощью AES cipher
    decoded_bytes = cipher.decrypt(bytes)
    
    # конвертация декодированных байтов в строку
    decoded_string = decoded_bytes.decode('utf-8')
    # decoded_string = decoded_bytes.decode('utf-8')
    text_without_hex = ''.join(['' if ord(c) < 32 or ord(c) > 126 else c for c in decoded_string])
    parsed = json.loads(text_without_hex)
    prettyPrint = json.dumps(parsed, indent=4)
    resultWindow(prettyPrint, ivStr)
def encodeConfig(plaintext, key, iv):
    key_bytes = bytes.fromhex(key)
    iv_bytes = bytes.fromhex(iv)
    block_size = AES.block_size
    padded_plaintext = plaintext.encode('utf-8') + (block_size - len(plaintext) % block_size) * chr(block_size - len(plaintext) % block_size).encode('utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    ciphertext = cipher.encrypt(padded_plaintext)
    encoded_ciphertext = ciphertext.hex()
    
    prettyPrint = '{' + '\n\t"data": {\n\t\t"dataHex": ' + f'"{encoded_ciphertext}",\n\t\t"ivHex": ' + f'"{iv}"' + '\n\t}' + '}'
    startMenu(prettyPrint)
def startMenu(textTo): 
    layout =  [
        [sg.Input(size=(55,1), default_text=keyMain, key='key', enable_events=True,
                  readonly=True, disabled=True), sg.Text("64-byte key", text_color='green')],

        # [sg.Combo(keyMain, default_value=keyMain[0], key='key', enable_events=True), 
        #  sg.Text("64-byte key", text_color='green')],

        [sg.Multiline(f"""{textTo}""", size=(70,13), key='mLine', focus=True)],
        [sg.Button('decode', size=(12, 1)), sg.CloseButton('Close', size=(12, 1))]
    ]
    
    window = sg.Window('encoded', layout, no_titlebar=False, grab_anywhere=True)
    while True:
        event, value = window.read(close=True)
        
        if event == 'decode':
            
            data = json.loads(value['mLine'])
            ivMain = data['data']['ivHex']
            decodeConfig(data['data']['dataHex'], keyMain, ivMain)
        
        if event in ('Close', None) or event == sg.WIN_CLOSED:
            try:
                exit(0)
            except:
                break
        window.close()
def resultWindow(resultText, iv):
    def get_text():
        getText = text.get("1.0", "end-1c")
        root.destroy()
        encodeConfig(getText, keyMain, iv)
        return getText      
    def save_text():
        getText = text.get("1.0", "end-1c")
        try:
            path = filedialog.asksaveasfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
            root.title('remoteConfig ' + path)
        except:
            return   
        with open(path, 'w') as f:
            f.write(getText)  
    def info():
        sg.popup_ok('Ctr + F --- set cursor\nCtr + S --- find text\nCtr + X --- clear\nCtr + V --- clear + find text', no_titlebar=1, grab_anywhere=1)
        
    #to create a window
    #root window is the parent window
    root = Tk()
    fram = Frame(root)
    
    root.title('RemoteConfig v.0.21')
    root.geometry("700x900+700+40")
    
    #saveas button
    buttSave = Button(fram, text='Save as', command=save_text)
    buttSave.pack(side=LEFT)

    buttInfo = Button(fram, text='Info', command=info)
    buttInfo.pack(side=LEFT)


    #adding label to search box
    Label(fram,text='Text to find: ',).pack(side=LEFT)
    
    #adding of single line text box
    edit = Entry(fram, width=40)

    #positioning of text box
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    
    #setting focus
    edit.focus_set()
    
    buttAdditional = Button(fram, text='Methods', bg='light blue') 
    buttAdditional.pack(side=RIGHT)
# =================================================================
    # encode back
    buttEncode = Button(fram, text='Encode', command=get_text, bg='red')
    buttEncode.pack(side=RIGHT)
# =================================================================
    buttClear = Button(fram, text='Clear', bg='yellow') 
    buttClear.pack(side=RIGHT)
    
    buttFind = Button(fram, text='Find', bg='#248c0f') 
    buttFind.pack(side=RIGHT)
    
    fram.pack(side=TOP)

    #  scrollBar
    v = Scrollbar(root, orient = 'vertical')
    v.pack(side=RIGHT, fill = 'y')
    
    #text box in root window
    text = Text(root, height=40, width=70, font=('Consolas',14), yscrollcommand=v.set)
    v.config(command=text.yview)
    text.pack(expand=True)
    # text.insert('1.0',open("C:\\Users\\frolov.an\\Desktop\\testHex.txt", 'r').read())
    text.insert("1.0", resultText)
        
    def clear():
        text.tag_remove('found', '1.0', END)
        edit.delete(0, END)
    def find():
        #remove tag 'found' from index 1 to END
        text.tag_remove('found', '1.0', END)
        
        #returns to widget currently in focus
        text_to_search = edit.get().split(' ')[0]
        if text_to_search:
            idx = '1.0'
            while 1:
                #searches for desired string from index 1
                idx = text.search(text_to_search, idx, nocase=1, stopindex=END)
                if not idx: break
                
                #last index sum of current index and
                #length of text
                lastidx = '%s+%dc' % (idx, len(text_to_search))
                
                #overwrite 'Found' at idx
                text.tag_add('found', idx, lastidx)
                idx = lastidx
                # text.mark_set("insert", lastidx)
            
            #mark located string as red
            text.tag_config('found', background='yellow', selectbackground='black')
            text.see(lastidx)

        edit.focus_set()
    def press_f(e):
        edit.focus_set()
        edit.selection_range(0, END)
    def press_v(e):
        find()
    def press_s(e):
        find()
    def press_x(e):
        clear()
    
    def additionalWindow():
        root_b=Tk()
        root_b.title('RemoteConfig Methods')
        sizex = 400
        sizey = 750
        posx  = 1300
        posy  = 80
        root_b.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
        
        # itemsforlistbox=['true','false','isAllowedCustomPhoneCodeInput = true','isAllowedChangePasswordWithoutPhone']
        itemsforlistbox = [ "hasSnapshot",
                            "ReferalLink",
                            'ReferalLink',
                            'isBettingEnabled',
                            'BettingEnabledGeo',
                            '-------------------------------------',
                            '[Авторизация]',
                            '-------------------------------------',
                            'isAllowedLoginByEmailAndId',	
                            'isDefaultLoginByPhone',			
                            'isAllowedLoginByLogin',
                            'isAllowedLoginByPhone',			
                            "isAllowedCustomPhoneCodeInput",	
                            'isAllowedLoginBySocial',			
                            'isAllowedChangePasswordWithoutPhone',		
                            'RestorePasswordAllowedCountries',	
                            'RestorePasswordForbiddenCountries',			
                            'isAllowedLoginByQr',
                            '-------------------------------------',
                            '[Регистрация]',
                            '-------------------------------------',                           
                            'fullRegPersonalDataHeaderIndex',
                            'fullRegAccountSettingsHeaderIndex',
                            'minimumAge = 18',
                            'linkToRules = ""',
                            'linkToPrivacy = ""',
                            '-------------------------------------',
                            '[Популярное]',
                            '-------------------------------------',
                            'hasAllowedAppWithoutAuth = true',
                            'hasAllowedAppOnlyWithActivatePhone = true',
                            'hasBlockAuthUprid = false',
                            'hasAlertPopular = false',
                            'hasPopularBalance = true',
                            'hasPopularSearch = true',
                            'popularSportsCount = 20',
                            'hasPopularGamesCarusel = true',
                            'hasBanners = true',
                            'popularTab',
                            'live',
                            'line',
                            'esports',
                            'xgames',
                            'slots',
                            'livecasino',
                            'virtual',
                            'champslive',
                            'champsline',
                            'hasMainscreenSettings = true',
                            'hasDirectMessages = true',
                            '-------------------------------------',
                            'Избранное + Просмотрено',
                            '-------------------------------------',
                            'hasSectionXGames = true',
                            'hasViewed = true',
                            'hasFollowed = true',
                            '-------------------------------------',
                            'Купон',
                            '-------------------------------------',
                            'paymentHost',
                            'hasAccumulatorOfTheDay = true',
                            'hasCouponGenerator = true',
                            'hasUploadCoupon = true',
                            'hasPromocodes = true',
                            'hasOrdersBets = true',
                            'hasVipBet = true',
                            'hasAdvancedBets = true',
                            'hasTaxSpoilerDefault = false',
                            '-------------------------------------',
                            'Типы ставок',
                            '-------------------------------------',
                            'hasSingleBet = true',
                            'hasAccumulatorBet = true',
                            'hasSystemBet = true',
                            'hasLuckyBet = true',
                            'hasChainBet = true',
                            'hasPatentBet = true',
                            'hasMultiBet = true',
                            'hasConditionalBet = true',
                            'hasAntiAccumulatorBet = true',
                            'hasMultiSingleBet = true',
                            '-------------------------------------',
                            'История ставок',
                            '-------------------------------------',
                            'hasSectionToto = true',
                            'hasOrdersBets = true',
                            'hasHistoryCasino = true',
                            'hasHistoryUncalculated = true',
                            'hasHistoryHide = true',
                            'bettingHistoryPeriod = 30',
                            'hasHistoryPeriodFilter = true',
                            'hasCouponPrint = true',
                            'hasSharingCouponPicture = true',
                            'hasHistoryToEmail = true',
                            'hasBetEdit = true',
                            'hasBetAutoSell = true',
                            'hasBetInsure = true',
                            'hasBetSellFull = true',
                            'hasBetSellPart = true',
                            'hasPowerBet = true',
                            'hasBetSellRoundValue = true',
                            'hasHideBets = true',
                            'hasHistoryPossibleWin = false',
                            '-------------------------------------',
                            '[Меню - Топ]',
                            '-------------------------------------',    
                            'hasCyberSport = true',
                            'hasSectionVirtual = false',
                            'hasSectionXGames = true',
                            'hasSectionSupport = true',
                            'hasAuthenticator = false',
                            'hasPromotionsTop = false',
                            'hasSectionPromoTop = false',
                            'hasSportCashback = false',
                            'hasJackpotToto = false',
                            'hasCyberSport = true',
                            'hasSectionXGames = true',
                            'hasSectionSupport = true',
                            'hasAuthenticator = false',
                            '-------------------------------------',
                            '[Спорт]',
                            '-------------------------------------',    
                            'hasCyberVirtualTab = true',
                            'hasAccumulatorOfTheDay = true',
                            'hasZone = true',
                            'hasStream = true',
                            'hasCyberSport = true',
                            'hasCyberVirtualTab = true',
                            'hasCyberCyberStreamTab = true',
                            'hasSportGamesTV = true',
                            'hasResults = true',
                            'hasNationalTeamBet = true',
                            '-------------------------------------',
                            '[Казино]',
                            '-------------------------------------',
                            'hasSectionCasino = true',
                            'hasMyCasino = true',
                            'hasVipCashback = true',
                            'hasCategoryCasino = true',
                            'hasTournamentsCasino = true',
                            'hasNativeTournamentsCasino = false',
                            'hasPromoCasino = true',
                            'hasTvBetCasinoMenu = false',
                            'hasProvidersCasino = true',
                            
                            'hasSectionVirtual = false',
                            
                            '-------------------------------------',
                            '[Нижнее меню Казино]',
                            '-------------------------------------',                            
                            'hasPromoCasinoMenu = true',
                            'hasFavoritesCasinoMenu = true',
                            'hasMyCasino = true',
                            'hasProvidersCasinoMenu = true',
                            'hasCategoryCasinoMenu = true',
                            '-------------------------------------',
                            '[Games]',
                            '-------------------------------------',                                        
                            'hasSectionXGames = true',
                            'hasIframeGames = true',
                            'xGamesName = ""',
                            'hasNewYearGame = false',
                            'hasXGamesPromo = true',
                            'hasLuckyWheel = true',
                            'hasXGamesBonuses = true',
                            'hasDailyQuest = true',
                            'hasWicklyReward = true',
                            'hasDailyTournament = true',
                            'hasXGamesBingo = true',
                            'hasXGamesJackpot = true',
                            'hasXGamesCashback = true',
                            'hasXGamesFavorite = true',
                            '-------------------------------------',
                            '[Личный кабинет]',
                            '-------------------------------------',    
                            'isAllowedEditPersonalInfo = true',
                            'isAllowedLoginByLogin = false',
                            'isAllowedAddEmail = true',
                            'isAllowedAddPhone = true',
                            'hasResetPhoneBySupport = false',
                            'isAllowedEditPhone = true',
                            'isAllowedPasswordChange = true',
                            'isAllowedChangePasswordWithoutPhone = false',
                            'isAllowedPersonalInfo = true',
                            'hasIINPersonal = false',
                            'isAllowedPasswordRecoveryByEmailOnly = true',
                            'HideResidencePersonalInfo',
                            '-------------------------------------',
                            '[Promo]',
                            '-------------------------------------',
                            'hasSectionPromo = true',
                            'hasSectionPromocodes = true',
                            'hasPromocodes = true',
                            'hasPromoShop = true',
                            'hasPromoPoints = true',
                            'hasPromoRequest = true',
                            'hasPromocodes = true',
                            'hasPromoRecommends = true',
                            'hasBonusGames = true',
                            'hasBonusGames = true',
                            'hasBonusGamesForPTSOnly = false',
                            'hasPromoPoints = true',
                            'hasSectionPromoCashback = true',
                            'hasSectionPromoCashback = true',
                            'hasCashbackPlacedBets = true',
                            'hasCashbackAccountBalance = true',
                            'hasSportCashback = false',
                            'hasVipCashback = true',
                            'hasPromoParticipation = true',
                            'hasSectionWelcomeBonus = false',
                            'hasSectionBonuses = true',
                            'hasSectionVIPClub = false',
                            'hasReferralProgram = false',
                            'hasAuthenticator = false',
                            '-------------------------------------',
                            '[ТОТО]',
                            '-------------------------------------',  
                            'hasSectionToto = true',
                            'TotoName = TOTO',
                            '',
                            'hasJackpotToto = false',
                            'hasFinancial = true',
                            'hasBetConstructor = true',
                            '-------------------------------------',
                            '[Сканер купонов]',
                            '-------------------------------------',  
                            'hasSectionBetslipScanner = true',
                            'hasBetslipScannerNumber = true',
                            'hasBetslipScannerPhoto = true',
                            'hasSectionToto = true',
                            '-------------------------------------',
                            '[Поддержка]',
                            '-------------------------------------',  
                            'hasSectionSupport = true',
                            'SupHelperSiteId = ""',
                            'hasCallBack = true',
                            'isAllowedCallBackCustomPhoneCodeInput = false',
                            'CallBackLangNotSupport = string_array',
                            'hasSIP = true',
                            'SipLangNotSupport = string_array',
                            'hasInfoContacts = true',
                            '-------------------------------------',
                            '[Инфо]',
                            '-------------------------------------',
                            'hasSectionInfo = true',
                            'hasInfoAboutUs = true',
                            'hasInfoSocials = false',
                            'hasInfoContacts = true',
                            'hasInfoRules = true',
                            'linkToRules = ""',
                            'hasResponsibleRules = false',
                            'linkToResponsible = ""',
                            'hasInfoLicense = true',
                            'hasInfoAwards = false',
                            'hasInfoPayments = true',
                            'hasInfoHowBet = true',
                            'hasInfoPartners = false',
                            'linkToOfficeMap = ""',
                            'hasInfoProcedures = false',
                            'linkToProcedures = ""',
                            'hasInfoComplaints = false',
                            'linkToComplaints = ""',
                            'hasInfoPrivacy = true',
                            'linkToPrivacy = ""',
                            'hasInfoStopList = false',
                            'linkToStopList = ""',
                            'hasInfoGDPR = false',
                            'linkToGDPR = ""',
                            'linktoUSSDinstruction = ""',
                            '-------------------------------------',
                            '[Управление счетом]',
                            '-------------------------------------',  
                            'BlockDepositUpridStatus = false',
                            'BlockWithdrawUpridStatus = false',
                            'BlockDepositCupis = false',
                            'BlockWithdrawCupis = false',
                            'VerificationNeed',
                            '-------------------------------------',
                            '[Безопасность]',
                            '-------------------------------------',                             
                            'hasSectionSecurity = true',
                            'hasAuthenticator = false',
                            '-------------------------------------',
                            '[Настройки ставок]',
                            '-------------------------------------',   
                            'isAvailableAutomax = true',
                            'hasVipBet = true',
                            'hasOrdersBets = true',
                            'hasOrdersBets = true',
                            '-------------------------------------',
                            '[Настройки приложения]',
                            '-------------------------------------',   
                            'isAllowedAddPhone = true',
                            'isAllowedAddEmail = true',
                            'isAllowedNewsToEmail = true',
                            'isAllowedBetsResultToEmail = false',
                            'hasBanners = true',
                            'hasShakeSection = false',
                            'hasAccumulatorOfTheDay = true',
                            'hasSectionXGames = true',
                            'hasSectionCasino = true',
                            '-------------------------------------',
                            '[Дополнительно]',
                            '-------------------------------------',  
                            'hasActualDomain = true',
                            'paymentHost =""',
                            'isAllowedProxySettings = true',
                            'hasSocial = true',
                            'hasGoogleSocial = false',
                            'hasVKontakteSocial = false',
                            'hasTelegramSocial = false',
                            'hasMailruSocial = false',
                            'hasOdnoklassnikiSocial = false',
                            'hasAppleIDSocial = false',
                            'hasYandexSocial = false',
                            'isAllowedLoginByQr = true',
                            'isNeedCheckEnabledPushForCustomerIO = false',
                            'isNeedSendPushAttributeToCustomerIO',
                            'hasAppSharingByLink = true',
                            'hasAppSharingByQr = true',
                            'hasOnboarding = false',
                            '',
                            '',
                            '',
                            '',
                            
   ]

        def CurSelet(evt):
            value=str((mylistbox.get(mylistbox.curselection())))
            # print (value)
            edit.delete(0, END)
            edit.focus_set()
            edit.insert(0, value)
            find()

            # additionalWindow_findElement()
            # return value
        
        mylistbox=Listbox(root_b, width=41, height=75,font=('Consolas',13), selectmode=SINGLE)
        mylistbox.bind('<<ListboxSelect>>', CurSelet)
        mylistbox.place(x=32,y=90)
        mylistbox.pack(side = LEFT, fill = BOTH)

        
        scrollbar = Scrollbar(root_b)
        scrollbar.pack(side = RIGHT, fill = BOTH)
        
        for items in itemsforlistbox:
            mylistbox.insert(END,items)

        mylistbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = mylistbox.yview)
        
        root_b.mainloop()
    
    root.bind('<Control-f>', press_f)
    root.bind('<Control-v>', press_v)
    root.bind('<Control-x>', press_x)
    root.bind('<Control-s>', press_s)
    
    buttEncode.config(command=get_text)
    buttClear.config(command=clear)
    buttFind.config(command=find)
    buttAdditional.config(command=additionalWindow)
    
    root.mainloop()
    root.destroy()
def hex_main():
    check_language()
    startMenu('')

if __name__ == '__main__':
    sg.theme('DarkGrey15')
    scope = ['https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
            ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Характеристики (сайты и приложения)").sheet1
    partners = create_partner_list()
    partner_name = get_partner_names()[0]
    
    
    show_tablet()