# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import logging
# import os

# # Set up logging
# logging.basicConfig(filename='whatsapp_automator.log', level=logging.DEBUG, 
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# # Initialize Chrome WebDriver
# try:
#     # Use chromedriver.exe in C:\Users\Momina\Desktop\WhatsApp Automation
#     service = Service('chromedriver.exe')
#     driver = webdriver.Chrome(service=service)
#     driver.maximize_window()
#     logging.info(f"ChromeDriver initialized successfully. Chrome version: {driver.capabilities['browserVersion']}")
#     print(f"Chrome version: {driver.capabilities['browserVersion']}")
# except Exception as e:
#     logging.error(f"Failed to initialize ChromeDriver: {e}")
#     print(f"Error starting Chrome: {e}")
#     exit()

# # Open WhatsApp Web
# driver.get("https://web.whatsapp.com")
# logging.info("Opened WhatsApp Web")
# print("Please scan the QR code")

# # Wait for login (check for QR code absence and chat list presence)
# try:
#     WebDriverWait(driver, 60).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1n2onr6"))
#     )
#     WebDriverWait(driver, 10).until(
#         EC.invisibility_of_element_located((By.CSS_SELECTOR, "canvas[aria-label='Scan this QR code to link a device!']"))
#     )
#     logging.info("Logged in successfully")
#     print("Logged in successfully")
# except:
#     logging.error("Login failed or timed out")
#     print("Login failed or timed out")
#     driver.quit()
#     exit()

# # Store the last top chat to avoid sending multiple messages to the same chat
# last_top_chat = None

# try:
#     while True:
#         try:
#             # Find all chats in the sidebar
#             chats = WebDriverWait(driver, 10).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.x1n2onr6 > div[tabindex='-1']"))
#             )
#             top_chat = chats[0]  # First chat is at the top
#             top_chat_title = top_chat.find_element(By.CSS_SELECTOR, "span[title]").get_attribute("title")

#             # Check if the top chat is new (different from the last one)
#             if top_chat_title != last_top_chat:
#                 try:
#                     # Check for unread message indicator
#                     top_chat.find_element(By.CSS_SELECTOR, "div._ak8i span[aria-label*='unread message']")
#                     logging.info(f"New unread message detected in chat: {top_chat_title}")
#                     print(f"New unread message detected in chat: {top_chat_title}")

#                     # Click the top chat
#                     top_chat.click()

#                     # Find the latest message text
#                     messages = WebDriverWait(driver, 5).until(
#                         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.copyable-text span._ao3e"))
#                     )
#                     latest_message = messages[-1].text.strip()  # Last message, stripped of whitespace

#                     # Skip if the message is empty (e.g., images, emojis)
#                     if not latest_message:
#                         logging.info(f"Latest message in {top_chat_title} is empty, skipping")
#                         print(f"Latest message in {top_chat_title} is empty, skipping")
#                         last_top_chat = top_chat_title
#                         continue

#                     # Find the message input box
#                     input_box = WebDriverWait(driver, 5).until(
#                         EC.presence_of_element_located((By.CSS_SELECTOR, "div._ak1r div[contenteditable='true'][data-tab='10']"))
#                     )
#                     # Clear any existing text
#                     input_box.clear()
#                     # Send custom message with extracted text
#                     reply = f"Hi hope you are doing fine. Did you ask {latest_message}"
#                     input_box.send_keys(reply + Keys.ENTER)
#                     logging.info(f"Sent message to {top_chat_title}: {reply}")
#                     print(f"Sent message to {top_chat_title}: {reply}")

#                     # Update last top chat
#                     last_top_chat = top_chat_title
#                 except:
#                     # No unread messages or not a new message, skip
#                     logging.info(f"Top chat {top_chat_title} has no new unread messages, skipping")
#                     print(f"Top chat {top_chat_title} has no new unread messages, skipping")
#                     last_top_chat = top_chat_title
#             # Wait briefly before checking again
#             time.sleep(2)
#         except Exception as e:
#             logging.error(f"Error: {e}")
#             print(f"Error: {e}")
#             time.sleep(5)  # Wait before retrying
# except KeyboardInterrupt:
#     logging.info("Script stopped by user")
#     print("Stopping script...")
#     driver.quit()
#     exit()

# ====================================================================================================================
# WhatsApp Automation Script (WORKING PERFECTLY)
# ====================================================================================================================

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import logging
# import os

# # Set up logging
# logging.basicConfig(filename='whatsapp_automator.log', level=logging.DEBUG, 
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# # Initialize Chrome WebDriver
# try:
#     service = Service('chromedriver.exe')
#     driver = webdriver.Chrome(service=service)
#     driver.maximize_window()
#     logging.info(f"ChromeDriver initialized successfully. Chrome version: {driver.capabilities['browserVersion']}")
#     print(f"Chrome version: {driver.capabilities['browserVersion']}")
# except Exception as e:
#     logging.error(f"Failed to initialize ChromeDriver: {e}")
#     print(f"Error starting Chrome: {e}")
#     exit()

# # Open WhatsApp Web
# driver.get("https://web.whatsapp.com")
# logging.info("Opened WhatsApp Web")
# print("Please scan the QR code")

# # Wait for login
# try:
#     WebDriverWait(driver, 60).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1n2onr6"))
#     )
#     WebDriverWait(driver, 10).until(
#         EC.invisibility_of_element_located((By.CSS_SELECTOR, "canvas[aria-label='Scan this QR code to link a device!']"))
#     )
#     logging.info("Logged in successfully")
#     print("Logged in successfully")
# except:
#     logging.error("Login failed or timed out")
#     print("Login failed or timed out")
#     driver.quit()
#     exit()

# # Track active chat and last message
# active_chat_title = None
# replied_chats = set()

# last_message_text = None

# try:
#     while True:
#         try:
#             # Find all chats
#             chats = WebDriverWait(driver, 10).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.x1n2onr6 > div[tabindex='-1']"))
#             )
#             top_chat = chats[0]
#             top_chat_title = top_chat.find_element(By.CSS_SELECTOR, "span[title]").get_attribute("title")

#             # Check if top chat has unread messages
#             try:
#                 top_chat.find_element(By.CSS_SELECTOR, "div._ak8i span[aria-label*='unread message']")
#                 is_unread = True
#             except:
#                 is_unread = False

#             # Process chat if it's new or the active chat with a new message
#             if is_unread or top_chat_title == active_chat_title:
#                 top_chat.click()

#                 # Get latest message
#                 messages = WebDriverWait(driver, 5).until(
#                     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.copyable-text span._ao3e"))
#                 )
#                 latest_message = messages[-1].text.strip()

#                 # Skip if message is empty or same as last processed
#                 if not latest_message or latest_message == last_message_text:
#                     logging.info(f"Skipping chat {top_chat_title}: Empty or same message")
#                     print(f"Skipping chat {top_chat_title}: Empty or same message")
#                     time.sleep(2)
#                     continue

#                 # Find input box
#                 input_box = WebDriverWait(driver, 5).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, "div._ak1r div[contenteditable='true'][data-tab='10']"))
#                 )
#                 input_box.clear()

#                 # Determine reply
#                 if top_chat_title != active_chat_title and is_unread:
#                     # New chat: Initial reply
#                     reply = f"Hi hope you are doing fine. Did you ask {latest_message}"
#                     active_chat_title = top_chat_title
#                 else:
#                     # Same chat: Follow-up reply
#                     reply = "I am sorry I can help you with it"

#                 # Send reply
#                 input_box.send_keys(reply + Keys.ENTER)
#                 logging.info(f"Sent message to {top_chat_title}: {reply}")
#                 print(f"Sent message to {top_chat_title}: {reply}")

#                 # Update last message
#                 last_message_text = latest_message

#             else:
#                 logging.info(f"Top chat {top_chat_title} has no new unread messages, skipping")
#                 print(f"Top chat {top_chat_title} has no new unread messages, skipping")

#             time.sleep(2)
#         except Exception as e:
#             logging.error(f"Error: {e}")
#             print(f"Error: {e}")
#             time.sleep(5)
# except KeyboardInterrupt:
#     logging.info("Script stopped by user")
#     print("Stopping script...")
#     driver.quit()
#     exit()


# ====================================================================================================================
# EXPERIMENT NO. 1 SUCCESS (REPLYING TO UNREAD MESSAGES BUT NOT FROM ALREADY OPENED CHAT)
# ====================================================================================================================



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from groq import Groq
# import time
# import logging
# import os

# # Set up logging
# logging.basicConfig(filename='whatsapp_automator.log', level=logging.DEBUG, 
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# # Initialize Groq client with hardcoded API key
# try:
#     groq_client = Groq(api_key="GROQ_API")
#     logging.info("Groq client initialized successfully")
#     print("Groq client initialized successfully")
# except Exception as e:
#     logging.error(f"Failed to initialize Groq client: {e}")
#     print(f"Error initializing Groq client: {e}")
#     exit()

# # Initialize Chrome WebDriver
# try:
#     service = Service('chromedriver.exe')
#     options = webdriver.ChromeOptions()
#     options.add_argument('--log-level=3')  # Suppress verbose logs
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.maximize_window()
#     logging.info(f"ChromeDriver initialized successfully. Chrome version: {driver.capabilities['browserVersion']}")
#     print(f"Chrome version: {driver.capabilities['browserVersion']}")
# except Exception as e:
#     logging.error(f"Failed to initialize ChromeDriver: {e}")
#     print(f"Error starting Chrome: {e}")
#     exit()

# # Open WhatsApp Web
# driver.get("https://web.whatsapp.com")
# logging.info("Opened WhatsApp Web")
# print("Please scan the QR code")

# # Wait for login
# try:
#     WebDriverWait(driver, 60).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1n2onr6"))
#     )
#     WebDriverWait(driver, 10).until(
#         EC.invisibility_of_element_located((By.CSS_SELECTOR, "canvas[aria-label='Scan this QR code to link a device!']"))
#     )
#     logging.info("Logged in successfully")
#     print("Logged in successfully")
# except:
#     logging.error("Login failed or timed out")
#     print("Login failed or timed out")
#     driver.quit()
#     exit()

# # Track active chat and last message
# active_chat_title = None
# replied_chats = set()
# last_message_text = None

# # System prompt for Groq to act as a friendly human
# SYSTEM_PROMPT = """
# You are a friendly, conversational human assistant. Respond to messages in a warm, approachable, and helpful tone, as if you're chatting with a friend. Keep your responses concise, natural, and relevant to the user's message. If the message is a question, provide a helpful answer or ask for clarification if needed. If it's a statement, acknowledge it kindly and offer assistance or continue the conversation naturally.
# """

# def get_groq_response(message):
#     """Generate a response using Groq API."""
#     try:
#         response = groq_client.chat.completions.create(
#             model="llama3-8b-8192",  # Use a valid model
#             messages=[
#                 {"role": "system", "content": SYSTEM_PROMPT},
#                 {"role": "user", "content": message}
#             ],
#             max_tokens=150,
#             temperature=0.7
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         logging.error(f"Groq API error: {e}")
#         print(f"Groq API error: {e}")
#         return "Sorry, I'm having trouble responding right now. Can you repeat that?"

# try:
#     while True:
#         try:
#             # Find all chats
#             chats = WebDriverWait(driver, 10).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.x1n2onr6 > div[tabindex='-1']"))
#             )
#             top_chat = chats[0]
#             top_chat_title = top_chat.find_element(By.CSS_SELECTOR, "span[title]").get_attribute("title")

#             # Check if top chat has unread messages
#             try:
#                 top_chat.find_element(By.CSS_SELECTOR, "span[aria-label*='unread message']")
#                 is_unread = True
#                 logging.info(f"Found unread messages in chat {top_chat_title}")
#                 print(f"Found unread messages in chat {top_chat_title}")
#             except:
#                 is_unread = False
#                 logging.info(f"No unread messages in chat {top_chat_title}")
#                 print(f"No unread messages in chat {top_chat_title}")

#             # Process chat if it's new or the active chat with a new message
#             if is_unread or top_chat_title == active_chat_title:
#                 top_chat.click()

#                 # Get latest message
#                 try:
#                     messages = WebDriverWait(driver, 10).until(
#                         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.message-in span._ao3e"))
#                     )
#                     if not messages:
#                         logging.info(f"Skipping chat {top_chat_title}: No valid messages found")
#                         print(f"Skipping chat {top_chat_title}: No valid messages found")
#                         time.sleep(2)
#                         continue
#                     latest_message = messages[-1].text.strip()

#                     # Skip if message is empty or same as last processed
#                     if not latest_message or latest_message == last_message_text:
#                         logging.info(f"Skipping chat {top_chat_title}: Empty or same message")
#                         print(f"Skipping chat {top_chat_title}: Empty or same message")
#                         time.sleep(2)
#                         continue
#                 except Exception as e:
#                     logging.error(f"Error fetching messages in chat {top_chat_title}: {e}")
#                     print(f"Error fetching messages in chat {top_chat_title}: {e}")
#                     time.sleep(5)
#                     continue

#                 # Find input box
#                 input_box = WebDriverWait(driver, 5).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, "div._ak1r div[contenteditable='true'][data-tab='10']"))
#                 )
#                 input_box.clear()

#                 # Generate reply using Groq
#                 if top_chat_title != active_chat_title and is_unread:
#                     # New chat: Initial reply
#                     prompt = f"Someone just messaged me: '{latest_message}'. Respond as if you're starting a friendly conversation."
#                     active_chat_title = top_chat_title
#                 else:
#                     # Same chat: Follow-up reply
#                     prompt = f"The conversation continues, and they just said: '{latest_message}'. Keep the friendly tone and respond naturally."

#                 reply = get_groq_response(prompt)

#                 # Send reply
#                 input_box.send_keys(reply + Keys.ENTER)
#                 logging.info(f"Sent message to {top_chat_title}: {reply}")
#                 print(f"Sent message to {top_chat_title}: {reply}")

#                 # Update last message
#                 last_message_text = latest_message

#             else:
#                 logging.info(f"Top chat {top_chat_title} has no new unread messages, skipping")
#                 print(f"Top chat {top_chat_title} has no new unread messages, skipping")

#             time.sleep(2)
#         except Exception as e:
#             logging.error(f"Error: {e}")
#             print(f"Error: {e}")
#             time.sleep(5)
# except KeyboardInterrupt:
#     logging.info("Script stopped by user")
#     print("Stopping script...")
#     driver.quit()
#     exit()
    
    
# ====================================================================================================================
# EXPERIMENT NO. 2 SUCCESS (REPLYING TO UNREAD MESSAGES FROM ALREADY OPENED CHAT AND NEW CHAT)
# ====================================================================================================================


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from groq import Groq
# import time
# import logging
# import os

# # Set up logging
# logging.basicConfig(filename='whatsapp_automator.log', level=logging.DEBUG, 
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# # Initialize Groq client
# try:
#     groq_client = Groq(api_key="GROQ_API")
#     logging.info("Groq client initialized successfully")
#     print("Groq client initialized successfully")
# except Exception as e:
#     logging.error(f"Failed to initialize Groq client: {e}")
#     print(f"Error initializing Groq client: {e}")
#     exit()

# # Initialize Chrome WebDriver
# try:
#     service = Service('chromedriver.exe')
#     options = webdriver.ChromeOptions()
#     options.add_argument('--log-level=3')
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.maximize_window()
#     logging.info(f"ChromeDriver initialized successfully. Chrome version: {driver.capabilities['browserVersion']}")
#     print(f"Chrome version: {driver.capabilities['browserVersion']}")
# except Exception as e:
#     logging.error(f"Failed to initialize ChromeDriver: {e}")
#     print(f"Error starting Chrome: {e}")
#     exit()

# # Open WhatsApp Web
# driver.get("https://web.whatsapp.com")
# logging.info("Opened WhatsApp Web")
# print("Please scan the QR code")

# # Wait for login
# try:
#     WebDriverWait(driver, 60).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1n2onr6"))
#     )
#     WebDriverWait(driver, 10).until(
#         EC.invisibility_of_element_located((By.CSS_SELECTOR, "canvas[aria-label='Scan this QR code to link a device!']"))
#     )
#     logging.info("Logged in successfully")
#     print("Logged in successfully")
# except Exception as e:
#     logging.error(f"Login failed or timed out: {e}")
#     print(f"Login failed or timed out: {e}")
#     driver.quit()
#     exit()

# # Track active chat and last message per chat
# active_chat_title = None
# chat_last_messages = {}  # Store last message and timestamp per chat

# # System prompt for Groq
# SYSTEM_PROMPT = """
# You are a friendly, conversational human assistant. Respond to messages in a warm, approachable, and helpful tone, as if you're chatting with a friend. Keep your responses concise, natural, and relevant to the user's message. If the message is a question, provide a helpful answer or ask for clarification if needed. If it's a statement, acknowledge it kindly and offer assistance or continue the conversation naturally.
# """

# def get_groq_response(message, is_new_chat):
#     try:
#         prompt = (
#             f"Someone just messaged me: '{message}'. Respond as if you're starting a friendly conversation."
#             if is_new_chat
#             else f"The conversation continues, and they just said: '{message}'. Keep the friendly tone and respond naturally. Dont behave as if you are starting a conversation."
#         )
#         response = groq_client.chat.completions.create(
#             model="llama3-8b-8192",
#             messages=[
#                 {"role": "system", "content": SYSTEM_PROMPT},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=150,
#             temperature=0.7
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         logging.error(f"Groq API error: {e}")
#         print(f"Groq API error: {e}")
#         return "Sorry, I'm having trouble responding right now. Can you repeat that?"

# def get_latest_message(chat_title):
#     """Get the latest message and its timestamp in the current chat."""
#     try:
#         messages = WebDriverWait(driver, 5).until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.message-in"))
#         )
#         if not messages:
#             logging.info(f"No valid messages found in chat {chat_title}")
#             return None, None
#         latest_message_elem = messages[-1]
#         message_text = latest_message_elem.find_element(By.CSS_SELECTOR, "span._ao3e").text.strip()
#         try:
#             timestamp = latest_message_elem.find_element(By.CSS_SELECTOR, "div[data-pre-plain-text]").get_attribute("data-pre-plain-text")
#         except:
#             timestamp = str(time.time())  # Fallback to current time
#         return message_text, timestamp
#     except Exception as e:
#         logging.error(f"Error fetching messages in chat {chat_title}: {e}")
#         return None, None

# def send_reply(chat_title, reply):
#     try:
#         input_box = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, "div._ak1r div[contenteditable='true'][data-tab='10']"))
#         )
#         input_box.clear()
#         input_box.send_keys(reply + Keys.ENTER)
#         logging.info(f"Sent message to {chat_title}: {reply}")
#         print(f"Sent message to {chat_title}: {reply}")
#     except Exception as e:
#         logging.error(f"Error sending reply in chat {chat_title}: {e}")
#         print(f"Error sending reply in chat {chat_title}: {e}")

# try:
#     while True:
#         try:
#             # Check the currently open chat first (if any)
#             if active_chat_title:
#                 latest_message, timestamp = get_latest_message(active_chat_title)
#                 if latest_message and (
#                     active_chat_title not in chat_last_messages or
#                     latest_message != chat_last_messages[active_chat_title]["message"] or
#                     timestamp != chat_last_messages[active_chat_title]["timestamp"]
#                 ):
#                     # New message in active chat
#                     is_new_chat = active_chat_title not in chat_last_messages
#                     reply = get_groq_response(latest_message, is_new_chat)
#                     send_reply(active_chat_title, reply)
#                     chat_last_messages[active_chat_title] = {
#                         "message": latest_message,
#                         "timestamp": timestamp
#                     }
#                 else:
#                     logging.info(f"No new messages in active chat {active_chat_title}")

#             # Find all chats and look for unread messages
#             chats = WebDriverWait(driver, 10).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.x1n2onr6 > div[tabindex='-1']"))
#             )
#             chat_with_unread = None
#             chat_title_with_unread = None

#             for chat in chats:
#                 try:
#                     chat_title = chat.find_element(By.CSS_SELECTOR, "span[title]").get_attribute("title")
#                     # Skip the active chat (already checked above)
#                     if chat_title == active_chat_title:
#                         continue
#                     # Check for green circle (unread messages)
#                     try:
#                         chat.find_element(By.CSS_SELECTOR, "span[aria-label*='unread message']")
#                         chat_with_unread = chat
#                         chat_title_with_unread = chat_title
#                         logging.info(f"Found unread messages in chat {chat_title}")
#                         break  # Process the first chat with unread messages
#                     except:
#                         continue
#                 except Exception as e:
#                     logging.error(f"Error checking chat {chat_title}: {e}")
#                     continue

#             # Process chat with unread messages if found
#             if chat_with_unread and chat_title_with_unread != active_chat_title:
#                 chat_with_unread.click()
#                 active_chat_title = chat_title_with_unread
#                 logging.info(f"Switched to new chat {active_chat_title}")
#                 time.sleep(1)  # Ensure chat loads

#                 # Get and process latest message
#                 latest_message, timestamp = get_latest_message(active_chat_title)
#                 if latest_message:
#                     is_new_chat = active_chat_title not in chat_last_messages
#                     reply = get_groq_response(latest_message, is_new_chat)
#                     send_reply(active_chat_title, reply)
#                     chat_last_messages[active_chat_title] = {
#                         "message": latest_message,
#                         "timestamp": timestamp
#                     }

#             time.sleep(3)  # Poll every 3 seconds
#         except Exception as e:
#             logging.error(f"Main loop error: {e}")
#             print(f"Main loop error: {e}")
#             time.sleep(5)
# except KeyboardInterrupt:
#     logging.info("Script stopped by user")
#     print("Stopping script...")
#     driver.quit()
#     exit()



# ====================================================================================================================
# EXPERIMENT NO. 3 (For Proxima) 
# # LIMITATIONS : REPLY ONE TEXT AT A TIME + HAS NO PAST REFRENCE + DO NOT REPLY ON PDF, VOICE NOTE, IMAGE
# ====================================================================================================================


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from groq import Groq
import time
import logging
import os
import json
import traceback

# Set up logging
logging.basicConfig(filename='whatsapp_automator.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Groq client
try:
    groq_client = Groq(api_key="GROQ_API")
    logging.info("Groq client initialized successfully")
    print("Groq client initialized successfully")
except Exception as e:
    logging.error(f"Failed to initialize Groq client: {e}")
    print(f"Error initializing Groq client: {e}")
    exit()

# Initialize Chrome WebDriver
try:
    service = Service('chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    logging.info(f"ChromeDriver initialized successfully. Chrome version: {driver.capabilities['browserVersion']}")
    print(f"Chrome version: {driver.capabilities['browserVersion']}")
except Exception as e:
    logging.error(f"Failed to initialize ChromeDriver: {e}")
    print(f"Error starting Chrome: {e}")
    exit()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
logging.info("Opened WhatsApp Web")
print("Please scan the QR code")

# Wait for login
try:
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1n2onr6"))
    )
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "canvas[aria-label='Scan this QR code to link a device!']"))
    )
    logging.info("Logged in successfully")
    print("Logged in successfully")
except Exception as e:
    logging.error(f"Login failed or timed out: {e}")
    print(f"Login failed or timed out: {e}")
    driver.quit()
    exit()

# Track active chat and last message per chat
active_chat_title = None
chat_last_messages = {}  # Store last message, timestamp, and data-id per chat
last_processed_time = {}  # Track last processed time per chat for cooldown

# System prompt for Groq
SYSTEM_PROMPT = """
You are a friendly, conversational human assistant. Respond to messages in a warm, approachable, and helpful tone, as if you're chatting with a friend. Keep your responses concise, natural, and relevant to the user's message. If the message is a question, provide a helpful answer or ask for clarification if needed. If it's a statement, acknowledge it kindly and offer assistance or continue the conversation naturally.
"""

def save_message(sender, message_content):
    message_data = {
        "sender": sender,
        "message": message_content
    }
    if os.path.exists("messages.json"):
        with open("messages.json", "r") as f:
            messages = json.load(f)
    else:
        messages = []
    messages.append(message_data)
    with open("messages.json", "w") as f:
        json.dump(messages, f, indent=4)

def get_groq_response(message, is_new_chat, message_type="text"):
    try:
        # Handle non-text messages
        if message_type in ["pdf", "voicenote", "image"]:
            return "Sorry, I'm a text-based virtual assistant and can't process PDFs, voice notes, or images. Please send a text-based query about Proxima AI, and I'll be happy to help!"

        prompt = (
            f"Someone just messaged me: '{message}'. Respond in a friendly tone and keep your reply under 100 words."
            if is_new_chat
            else f"The conversation continues, and they just said: '{message}'. Keep the friendly tone and reply naturally, but do not exceed 100 words."
        )

        response = groq_client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "system", "content": SYSTEM_PROMPT},
                      {"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"Groq API error: {e}")
        print(f"Groq API error: {e}")
        return "Sorry, I'm having trouble responding right now. Can you repeat that?"

# def get_latest_message(chat_title):
#     """Get the latest message and its timestamp in the current chat."""
#     try:
#         messages = WebDriverWait(driver, 5).until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.message-in"))
#         )
#         if not messages:
#             logging.info(f"No valid messages found in chat {chat_title}")
#             return None, None
#         latest_message_elem = messages[-1]
#         message_text = latest_message_elem.find_element(By.CSS_SELECTOR, "span._ao3e").text.strip()
#         try:
#             timestamp = latest_message_elem.find_element(By.CSS_SELECTOR, "div[data-pre-plain-text]").get_attribute("data-pre-plain-text")
#         except:
#             timestamp = str(time.time())  # Fallback to current time
#         return message_text, timestamp
#     except Exception as e:
#         logging.error(f"Error fetching messages in chat {chat_title}: {e}")
#         return None, None

def get_latest_message(chat_title):
    """Get the latest message, its type, timestamp, and data-id in the current chat."""
    try:
        messages = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.message-in"))
        )
        if not messages:
            logging.info(f"No valid messages found in chat {chat_title}")
            return None, None, None, None

        latest_message_elem = messages[-1]

        # Get data-id for unique message identification
        try:
            data_id = latest_message_elem.get_attribute("data-id")
        except:
            data_id = None
            logging.warning(f"Could not retrieve data-id for message in chat {chat_title}")

        # Check for message type
        message_type = "text"
        message_text = None

        # Check for voice note
        try:
            latest_message_elem.find_element(By.CSS_SELECTOR, "div._ak4a")  # Voice note container
            message_type = "voicenote"
            message_text = "Voice note"
            logging.info(f"Voice note detected in chat {chat_title}")
        except:
            pass

        # Check for image
        try:
            latest_message_elem.find_element(By.CSS_SELECTOR, "img.x15kfjtz")  # Image element
            message_type = "image"
            message_text = "Image"
            logging.info(f"Image detected in chat {chat_title}")
        except:
            pass

        # Check for PDF
        try:
            latest_message_elem.find_element(By.CSS_SELECTOR, "span[data-icon='document-PDF-icon']")  # PDF icon
            message_type = "pdf"
            message_text = "PDF"
            logging.info(f"PDF detected in chat {chat_title}")
        except:
            pass

        # Try to get text content (default case)
        if message_type == "text":
            try:
                message_text = latest_message_elem.find_element(By.CSS_SELECTOR, "span._ao3e").text.strip()
                if not message_text:
                    logging.warning(f"No valid text found in the latest message from chat {chat_title}")
                    return None, None, None, None
            except:
                logging.warning(f"No text found in the latest message from chat {chat_title}")
                return None, None, None, None

        # Get timestamp
        try:
            timestamp = latest_message_elem.find_element(By.CSS_SELECTOR, "span.x1rg5ohu.x16dsc37").text.strip()
            if not timestamp:
                timestamp = str(time.time())  # Fallback
                logging.warning(f"No timestamp found, using current time in chat {chat_title}")
        except:
            timestamp = str(time.time())  # Fallback to current time
            logging.warning(f"Failed to retrieve timestamp, using current time in chat {chat_title}")

        return message_text, message_type, timestamp, data_id

    except Exception as e:
        logging.error(f"Error fetching messages in chat {chat_title}: {e}\n{traceback.format_exc()}")
        return None, None, None, None

def send_reply(chat_title, reply):
    try:
        input_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div._ak1r div[contenteditable='true'][data-tab='10']"))
        )
        input_box.clear()
        input_box.send_keys(reply + Keys.ENTER)
        logging.info(f"Sent message to {chat_title}: {reply}")
        print(f"Sent message to {chat_title}: {reply}")
    except Exception as e:
        logging.error(f"Error sending reply in chat {chat_title}: {e}")
        print(f"Error sending reply in chat {chat_title}: {e}")

try:
    while True:
        try:
            # Check the currently open chat first (if any)
            if active_chat_title:
                latest_message, message_type, timestamp, data_id = get_latest_message(active_chat_title)
                
                # Check cooldown (prevent re-processing within 30 seconds)
                current_time = time.time()
                if active_chat_title in last_processed_time:
                    if current_time - last_processed_time[active_chat_title] < 30:
                        logging.debug(f"Skipping {active_chat_title} due to cooldown")
                        time.sleep(1)
                        continue
                
                if latest_message and (
                    active_chat_title not in chat_last_messages or
                    data_id != chat_last_messages.get(active_chat_title, {}).get("data_id") or
                    (latest_message != chat_last_messages[active_chat_title]["message"] and
                     timestamp != chat_last_messages[active_chat_title]["timestamp"])
                ):
                    # New message in active chat
                    is_new_chat = active_chat_title not in chat_last_messages
                    reply = get_groq_response(latest_message, is_new_chat, message_type)
                    send_reply(active_chat_title, reply)
                    chat_last_messages[active_chat_title] = {
                        "message": latest_message,
                        "timestamp": timestamp,
                        "data_id": data_id
                    }
                    last_processed_time[active_chat_title] = current_time
                    save_message(active_chat_title, latest_message)

            # Find all chats and look for unread messages
            chats = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.x1n2onr6 > div[tabindex='-1']"))
            )
            chat_with_unread = None
            chat_title_with_unread = None

            for chat in chats:
                try:
                    chat_title = chat.find_element(By.CSS_SELECTOR, "span[title]").get_attribute("title")
                    if chat_title == active_chat_title:
                        continue
                    try:
                        chat.find_element(By.CSS_SELECTOR, "span[aria-label*='unread message']")
                        chat_with_unread = chat
                        chat_title_with_unread = chat_title
                        logging.info(f"Found unread messages in chat {chat_title}")
                        break
                    except:
                        continue
                except Exception as e:
                    logging.error(f"Error checking chat {chat_title}: {e}")
                    continue

            # Process chat with unread messages if found
            if chat_with_unread and chat_title_with_unread != active_chat_title:
                chat_with_unread.click()
                active_chat_title = chat_title_with_unread
                logging.info(f"Switched to new chat {active_chat_title}")
                time.sleep(1)  # Ensure chat loads

                # Get and process latest message
                latest_message, message_type, timestamp, data_id = get_latest_message(active_chat_title)
                if latest_message:
                    is_new_chat = active_chat_title not in chat_last_messages
                    reply = get_groq_response(latest_message, is_new_chat, message_type)
                    send_reply(active_chat_title, reply)
                    chat_last_messages[active_chat_title] = {
                        "message": latest_message,
                        "timestamp": timestamp,
                        "data_id": data_id
                    }
                    last_processed_time[active_chat_title] = time.time()
                    save_message(active_chat_title, latest_message)

            time.sleep(1)  # Poll every 3 seconds
        except Exception as e:
            logging.error(f"Main loop error: {e}\n{traceback.format_exc()}")
            print(f"Main loop error: {e}")
            time.sleep(1)
except KeyboardInterrupt:
    logging.info("Script stopped by user")
    print("Stopping script...")
    driver.quit()
    exit()