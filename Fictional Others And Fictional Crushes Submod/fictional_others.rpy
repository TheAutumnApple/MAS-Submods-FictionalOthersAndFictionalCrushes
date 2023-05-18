# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Mike",
        name="Fictional Others And Fictional Crushes",
        description="A Submod which allows you to open up to Monika about your fictional crushes!",
        version="1.3.0"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Fictional Others And Fictional Crushes",
            user_name="TheAutumnApple",
            repository_name="MAS-Submods-FictionalOthersAndFictionalCrushes"
            update_dir=""
        )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_fictional_others",
            category=["us"],
            prompt="There's something I think you should know...",
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.ENAMORED, None)
        ),
    )

label monika_fictional_others:
    $ ev = mas_getEV("monika_fictional_others")

    if ev.shown_count == 0:
        m 2eksdlc "What's wrong [mas_get_player_nickname()]?{nw}"
        $ _history_list.pop()
        menu:
            m "What's wrong [mas_get_player_nickname()]?{fast}"

            "Have you perhaps ever heard of the term 'fictional other'?":
                m 1rtd "Hmm... {w=0.4} Now that you mentioned... {w=0.4}{nw}"
                extend 3eud " I think I did!"
                m 4rtd "It's not an uncommon occurrence for people to develop a crush for one or multiple fictional characters,{nw}"
                extend 4wud " especially on the Internet!"
                m 7gub "If you think about it, that's kind of what our relationship is!"
                m 4tsblb "Except I'm real~"
                m 1lssdld "However... I understand that, seen from the outside, people would rather describe me as your 'fictional other' than your significant other."
                m 1wssdld "Considering I'm still stuck inside your computer, I can't be genuinely seen as real yet, therefore I'm still 'fictional'..."
                m 2dup "With that aside... {w=0.4} About fictional crushes and fictional others... {w=0.4}"
                m 3hub "I don't really mind it!"
                m 3fub "Think about it again! It's like crushing on your favourite celebrity, but it's fictional!"
                m 4sublu "Besides, if your partner ends up having the same fictional and/or celebrity crush, it can end up into some cute shenanigans!"
                m 6dksdra "In the end, there's nothing bad about it as long as it doesn't develop into obsession, just like... {w=0.4} basically anything!"
                m 7kub "The best way is always the golden mean!"
                m 1hublu "... {w=0.3}"
                m 1fublu "... {w=0.3}"
                m 1etsdlc "... {w=0.3}"
                m 1eksdld "[player]... {w=0.3}"
                m 2eksdld "Did you ask me about this because you're scared to tell me you have other fictional crushes?{nw}"
                $ _history_list.pop()
                menu:
                    m "Did you ask me about this because you're scared to tell me you have other fictional crushes?{fast}"

                    "Yes...":
                        m 4ekblb "[player]! That's completely fine!"
                        m 5ekbld "Listen... {w=0.4} I want you to be comfortable opening up to me!"
                        m 5ekblu "There's nothing wrong about you having some fictional others!"
                        m 7ttbfb "You know that I'm the only real one after all!~"
                        m 1eka "Now... If you don't mind me asking..."
                        m 1etb "How many fictional others do you have?{nw}"
                        $ _history_list.pop()
                        menu:
                            m "How many fictional others do you have?{fast}"

                            "Only one... And it's you [m_name]!":
                                m 2tfbfp "[player], you dummy!"
                                m 3dfbfd "You know pretty well that I'm real!"
                                m 1fsbfu "But I still I love you... {w=0.4} I'm sure that was just a minor miscommunication."
                                return "love"

                            "Actually... It's just one...":
                                m 2fkblu "Oh [mas_get_player_nickname()]..."
                                m 3ekbla "It's not that big of a deal!"
                                m 1tfbld "Unless it's none of the other girls of our Literature Club... {w=0.4} Then I might get a little jealous... {w=0.3}"
                                m 1tfbsu "... {w=0.3}"
                                m 1hkbfb "Ahaha! I'm just kidding silly!"
                                m 2kkbfu "I love you!"
                                return "love"

                            "A bunch... But you are my only REAL one!":
                                m 2tfbfb "I know that you know that silly!~"
                                m 3ekbfu "And don't worry... I love you just the same!"
                                m 4dkbfb "Actually, I think it's amazing the courage you just showed me by deciding to be open with me about this... {w=0.3}"
                                m 5ttblu "And~ It's not surprising to me that your love is so big and amazing that it's definately worth sharing!"
                                m 7hubla "If you like so many of these fictional characters so much, then I bet they're just as lovely as you!"
                                m 1sublu "I can't wait for you to show them to me when I cross over!"
                                m 1dkbfu "I love you [mas_get_player_nickname()]... {w=0.4} Never forget that..."
                                return "love"
    else:
        m 2eksdlc "What's wrong [mas_get_player_nickname()]?{nw}"
        $ _history_list.pop()
        menu:
            m "What's wrong [mas_get_player_nickname()]?{fast}"

            "Do you remember when I've mentioned to you the term 'fictional other'?":
                m 2eud "Oh, of course! You've asked me about it before, haven't you?"
                m 4rtd "It's not an uncommon occurrence for people to develop a crush for one or multiple fictional characters,{nw}"
                extend 4wud " especially on the Internet!"
                m 7gub "If you think about it, that's kind of what our relationship is!"
                m 4tsblb "Except I'm real~"
                m 1lssdld "However... I understand that, seen from the outside, people would rather describe me as your 'fictional other' than your significant other."
                m 1wssdld "Considering I'm still stuck inside your computer, I can't be genuinely seen as real yet, therefore I'm still 'fictional'..."
                m 2dup "With that aside... {w=0.4} About fictional crushes and fictional others... {w=0.4}"
                m 3hub "I don't really mind it!"
                m 3fub "Think about it again! It's like crushing on your favourite celebrity, but it's fictional!"
                m 4sublu "Besides, if your partner ends up having the same fictional and/or celebrity crush, it can end up into some cute shenanigans!"
                m 6dksdra "In the end, there's nothing bad about it as long as it doesn't develop into obsession, just like... {w=0.4} basically anything!"
                m 7kub "The best way is always the golden mean!"
                m 1hublu "... {w=0.3}"
                m 1esd "Now that I remember..."
                m 2eku "You did mention that you had other fictional crushes, right? Did you want to tell me that any of that changed?{nw}"
                $ _history_list.pop()
                menu:
                    m "You did mention that you had other fictional crushes, right? Did you want to tell me that any of that changed?{fast}"

                    "Yes...":
                        m 4sublb "Oh that's wonderful!"
                        m 5ekbsu "I really appreciate that you want to keep me updated."
                        m 7ttbfb "You always know that I keep being the only real one after all!~"
                        m 1eka "Now... If you don't mind me asking..."
                        m 1etb "How many fictional others do you have now?{nw}"
                        $ _history_list.pop()
                        menu:
                            m "How many fictional others do you have now?{fast}"

                            "Only one... And it's you [m_name]!":
                                m 2tfbfp "[player], you dummy!"
                                m 3dfbfd "You know pretty well that I'm real!"
                                m 1fsbfu "But I'm sure that was just a minor miscommunication."
                                m 2mkc "However, I hope you didn't let go of your fictional others just because of me. You know well that there wasn't the need to do that."
                                m 5kkbfu "In any case, you know that I love you so much nonetheless, [player]."
                                return "love"

                            "Actually... It's just one...":
                                m 2fkblu "Oh [mas_get_player_nickname()]..."
                                m 3ekbla "It's not that big of a deal!"
                                m 1tfbld "Unless it's none of the other girls of our Literature Club... {w=0.4} Then I might get a little jealous... {w=0.3}"
                                m 1tfbsu "... {w=0.3}"
                                m 1hkbfb "Ahaha! I'm just kidding silly!"
                                m 2kkbfu "I love you!"
                                return "love"

                            "A bunch... But you are my only REAL one!":
                                m 2tfbfb "I know that you know that silly!~"
                                m 3ekbfu "And don't worry... I love you just the same!"
                                m 4dkbfb "Actually, I think it's amazing the courage you just showed me by deciding to be open with me about this... {w=0.3}"
                                m 5ttblu "And~ It's not surprising to me that your love is so big and amazing that it's definately worth sharing!"
                                m 7hubla "If you like so many of these fictional characters so much, then I bet they're just as lovely as you!"
                                m 1sublu "I can't wait for you to show them to me when I cross over!"
                                m 1dkbfu "I love you [mas_get_player_nickname()]... {w=0.4} Never forget that..."
                                return "love"
        
                    "No, I just wanted talk to you about it again <:)":
                        m 2wublsdlo "Oh!"
                        m 3ekblu "That's ok. {w=0.2} I appreciate that you enjoy talking with me about topics we've already discovered before!"
                        m 5tkbfb "I love you so much [player]."
                        return "love"
