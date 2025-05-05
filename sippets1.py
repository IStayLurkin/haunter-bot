PS F:\Projects\haun> .\generate_bot_commands.py
PS F:\Projects\haun> python .\generate_bot_commands.py
Current working directory: F:\Projects\haun

--- Code snippets to add to Kiba Bot's on_message function: ---


    elif content.startswith("!4chan_api_client"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "4chan_api_client" in TOOLS:
                result = TOOLS["4chan_api_client"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `4chan_api_client` not found.")
        return


    elif content.startswith("!afl"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "afl" in TOOLS:
                result = TOOLS["afl"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `afl` not found.")
        return


    elif content.startswith("!ahmia"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ahmia" in TOOLS:
                result = TOOLS["ahmia"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ahmia` not found.")
        return


    elif content.startswith("!aircrack_ng"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "aircrack_ng" in TOOLS:
                result = TOOLS["aircrack_ng"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `aircrack_ng` not found.")
        return


    elif content.startswith("!alienvault_otx"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "alienvault_otx" in TOOLS:
                result = TOOLS["alienvault_otx"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `alienvault_otx` not found.")
        return


    elif content.startswith("!amass"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "amass" in TOOLS:
                result = TOOLS["amass"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `amass` not found.")
        return


    elif content.startswith("!anchore_engine"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "anchore_engine" in TOOLS:
                result = TOOLS["anchore_engine"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `anchore_engine` not found.")
        return


    elif content.startswith("!angelcam"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "angelcam" in TOOLS:
                result = TOOLS["angelcam"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `angelcam` not found.")
        return


    elif content.startswith("!apktool"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "apktool" in TOOLS:
                result = TOOLS["apktool"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `apktool` not found.")
        return


    elif content.startswith("!aquatone"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "aquatone" in TOOLS:
                result = TOOLS["aquatone"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `aquatone` not found.")
        return


    elif content.startswith("!assetfinder"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "assetfinder" in TOOLS:
                result = TOOLS["assetfinder"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `assetfinder` not found.")
        return


    elif content.startswith("!autopsy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "autopsy" in TOOLS:
                result = TOOLS["autopsy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `autopsy` not found.")
        return


    elif content.startswith("!aws_boto3"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "aws_boto3" in TOOLS:
                result = TOOLS["aws_boto3"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `aws_boto3` not found.")
        return


    elif content.startswith("!azure_sdk"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "azure_sdk" in TOOLS:
                result = TOOLS["azure_sdk"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `azure_sdk` not found.")
        return


    elif content.startswith("!beef"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "beef" in TOOLS:
                result = TOOLS["beef"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `beef` not found.")
        return


    elif content.startswith("!bettercap"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "bettercap" in TOOLS:
                result = TOOLS["bettercap"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `bettercap` not found.")
        return


    elif content.startswith("!binary_ninja"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "binary_ninja" in TOOLS:
                result = TOOLS["binary_ninja"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `binary_ninja` not found.")
        return


    elif content.startswith("!bing_image_search"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "bing_image_search" in TOOLS:
                result = TOOLS["bing_image_search"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `bing_image_search` not found.")
        return


    elif content.startswith("!bing_maps"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "bing_maps" in TOOLS:
                result = TOOLS["bing_maps"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `bing_maps` not found.")
        return


    elif content.startswith("!binwalk"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "binwalk" in TOOLS:
                result = TOOLS["binwalk"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `binwalk` not found.")
        return


    elif content.startswith("!blockchair_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "blockchair_api" in TOOLS:
                result = TOOLS["blockchair_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `blockchair_api` not found.")
        return


    elif content.startswith("!bloom"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "bloom" in TOOLS:
                result = TOOLS["bloom"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `bloom` not found.")
        return


    elif content.startswith("!bluez"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "bluez" in TOOLS:
                result = TOOLS["bluez"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `bluez` not found.")
        return


    elif content.startswith("!burp_suite"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "burp_suite" in TOOLS:
                result = TOOLS["burp_suite"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `burp_suite` not found.")
        return


    elif content.startswith("!bus_pirate"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "bus_pirate" in TOOLS:
                result = TOOLS["bus_pirate"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `bus_pirate` not found.")
        return


    elif content.startswith("!camstreamer"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "camstreamer" in TOOLS:
                result = TOOLS["camstreamer"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `camstreamer` not found.")
        return


    elif content.startswith("!censys"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "censys" in TOOLS:
                result = TOOLS["censys"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `censys` not found.")
        return


    elif content.startswith("!chainalysis_reactor"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "chainalysis_reactor" in TOOLS:
                result = TOOLS["chainalysis_reactor"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `chainalysis_reactor` not found.")
        return


    elif content.startswith("!chipwhisperer"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "chipwhisperer" in TOOLS:
                result = TOOLS["chipwhisperer"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `chipwhisperer` not found.")
        return


    elif content.startswith("!clearbit"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "clearbit" in TOOLS:
                result = TOOLS["clearbit"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `clearbit` not found.")
        return


    elif content.startswith("!cmu_sphinx"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "cmu_sphinx" in TOOLS:
                result = TOOLS["cmu_sphinx"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `cmu_sphinx` not found.")
        return


    elif content.startswith("!cobalt_strike"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "cobalt_strike" in TOOLS:
                result = TOOLS["cobalt_strike"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `cobalt_strike` not found.")
        return


    elif content.startswith("!cosign"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "cosign" in TOOLS:
                result = TOOLS["cosign"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `cosign` not found.")
        return


    elif content.startswith("!creepy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "creepy" in TOOLS:
                result = TOOLS["creepy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `creepy` not found.")
        return


    elif content.startswith("!cve_search"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "cve_search" in TOOLS:
                result = TOOLS["cve_search"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `cve_search` not found.")
        return


    elif content.startswith("!cyberchef"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "cyberchef" in TOOLS:
                result = TOOLS["cyberchef"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `cyberchef` not found.")
        return


    elif content.startswith("!datasploit"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "datasploit" in TOOLS:
                result = TOOLS["datasploit"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `datasploit` not found.")
        return


    elif content.startswith("!dehashed"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "dehashed" in TOOLS:
                result = TOOLS["dehashed"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `dehashed` not found.")
        return


    elif content.startswith("!dependency_track_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "dependency_track_api" in TOOLS:
                result = TOOLS["dependency_track_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `dependency_track_api` not found.")
        return


    elif content.startswith("!dnsdumpster"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "dnsdumpster" in TOOLS:
                result = TOOLS["dnsdumpster"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `dnsdumpster` not found.")
        return


    elif content.startswith("!duckduckgo_images"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "duckduckgo_images" in TOOLS:
                result = TOOLS["duckduckgo_images"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `duckduckgo_images` not found.")
        return


    elif content.startswith("!elasticsearch"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "elasticsearch" in TOOLS:
                result = TOOLS["elasticsearch"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `elasticsearch` not found.")
        return


    elif content.startswith("!eleutherai_gpt_neo"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "eleutherai_gpt_neo" in TOOLS:
                result = TOOLS["eleutherai_gpt_neo"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `eleutherai_gpt_neo` not found.")
        return


    elif content.startswith("!eleutherai_gpt_neox"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "eleutherai_gpt_neox" in TOOLS:
                result = TOOLS["eleutherai_gpt_neox"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `eleutherai_gpt_neox` not found.")
        return


    elif content.startswith("!emailrep"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "emailrep" in TOOLS:
                result = TOOLS["emailrep"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `emailrep` not found.")
        return


    elif content.startswith("!esptool"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "esptool" in TOOLS:
                result = TOOLS["esptool"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `esptool` not found.")
        return


    elif content.startswith("!etherscan_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "etherscan_api" in TOOLS:
                result = TOOLS["etherscan_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `etherscan_api` not found.")
        return


    elif content.startswith("!exiftool"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "exiftool" in TOOLS:
                result = TOOLS["exiftool"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `exiftool` not found.")
        return


    elif content.startswith("!eyewitness"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "eyewitness" in TOOLS:
                result = TOOLS["eyewitness"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `eyewitness` not found.")
        return


    elif content.startswith("!face_recognition"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "face_recognition" in TOOLS:
                result = TOOLS["face_recognition"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `face_recognition` not found.")
        return


    elif content.startswith("!falcon"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "falcon" in TOOLS:
                result = TOOLS["falcon"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `falcon` not found.")
        return


    elif content.startswith("!flan_t5"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "flan_t5" in TOOLS:
                result = TOOLS["flan_t5"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `flan_t5` not found.")
        return


    elif content.startswith("!foca"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "foca" in TOOLS:
                result = TOOLS["foca"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `foca` not found.")
        return


    elif content.startswith("!frida"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "frida" in TOOLS:
                result = TOOLS["frida"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `frida` not found.")
        return


    elif content.startswith("!ftk_imager"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ftk_imager" in TOOLS:
                result = TOOLS["ftk_imager"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ftk_imager` not found.")
        return


    elif content.startswith("!gcp_sdk"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "gcp_sdk" in TOOLS:
                result = TOOLS["gcp_sdk"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `gcp_sdk` not found.")
        return


    elif content.startswith("!geoip2"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "geoip2" in TOOLS:
                result = TOOLS["geoip2"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `geoip2` not found.")
        return


    elif content.startswith("!geopy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "geopy" in TOOLS:
                result = TOOLS["geopy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `geopy` not found.")
        return


    elif content.startswith("!ghidra"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ghidra" in TOOLS:
                result = TOOLS["ghidra"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ghidra` not found.")
        return


    elif content.startswith("!ghunt"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ghunt" in TOOLS:
                result = TOOLS["ghunt"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ghunt` not found.")
        return


    elif content.startswith("!github_archive_spark"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "github_archive_spark" in TOOLS:
                result = TOOLS["github_archive_spark"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `github_archive_spark` not found.")
        return


    elif content.startswith("!gitleaks"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "gitleaks" in TOOLS:
                result = TOOLS["gitleaks"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `gitleaks` not found.")
        return


    elif content.startswith("!gnu_radio"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "gnu_radio" in TOOLS:
                result = TOOLS["gnu_radio"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `gnu_radio` not found.")
        return


    elif content.startswith("!google_geofencing_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "google_geofencing_api" in TOOLS:
                result = TOOLS["google_geofencing_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `google_geofencing_api` not found.")
        return


    elif content.startswith("!google_images_search"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "google_images_search" in TOOLS:
                result = TOOLS["google_images_search"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `google_images_search` not found.")
        return


    elif content.startswith("!google_speech_to_text"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "google_speech_to_text" in TOOLS:
                result = TOOLS["google_speech_to_text"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `google_speech_to_text` not found.")
        return


    elif content.startswith("!gophish"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "gophish" in TOOLS:
                result = TOOLS["gophish"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `gophish` not found.")
        return


    elif content.startswith("!gpt4all"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "gpt4all" in TOOLS:
                result = TOOLS["gpt4all"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `gpt4all` not found.")
        return


    elif content.startswith("!gpt_j"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "gpt_j" in TOOLS:
                result = TOOLS["gpt_j"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `gpt_j` not found.")
        return


    elif content.startswith("!greenbone_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "greenbone_api" in TOOLS:
                result = TOOLS["greenbone_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `greenbone_api` not found.")
        return


    elif content.startswith("!greyhat_warfare"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "greyhat_warfare" in TOOLS:
                result = TOOLS["greyhat_warfare"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `greyhat_warfare` not found.")
        return


    elif content.startswith("!harvester"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "harvester" in TOOLS:
                result = TOOLS["harvester"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `harvester` not found.")
        return


    elif content.startswith("!hashcat"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "hashcat" in TOOLS:
                result = TOOLS["hashcat"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `hashcat` not found.")
        return


    elif content.startswith("!hash_identifier"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "hash_identifier" in TOOLS:
                result = TOOLS["hash_identifier"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `hash_identifier` not found.")
        return


    elif content.startswith("!have_i_been_pwned"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "have_i_been_pwned" in TOOLS:
                result = TOOLS["have_i_been_pwned"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `have_i_been_pwned` not found.")
        return


    elif content.startswith("!hugging_face_transformers"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "hugging_face_transformers" in TOOLS:
                result = TOOLS["hugging_face_transformers"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `hugging_face_transformers` not found.")
        return


    elif content.startswith("!hunter_io"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "hunter_io" in TOOLS:
                result = TOOLS["hunter_io"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `hunter_io` not found.")
        return


    elif content.startswith("!hydra"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "hydra" in TOOLS:
                result = TOOLS["hydra"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `hydra` not found.")
        return


    elif content.startswith("!insecam"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "insecam" in TOOLS:
                result = TOOLS["insecam"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `insecam` not found.")
        return


    elif content.startswith("!inspy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "inspy" in TOOLS:
                result = TOOLS["inspy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `inspy` not found.")
        return


    elif content.startswith("!inteltechniques_tools"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "inteltechniques_tools" in TOOLS:
                result = TOOLS["inteltechniques_tools"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `inteltechniques_tools` not found.")
        return


    elif content.startswith("!ipify"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ipify" in TOOLS:
                result = TOOLS["ipify"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ipify` not found.")
        return


    elif content.startswith("!ipinfo"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ipinfo" in TOOLS:
                result = TOOLS["ipinfo"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ipinfo` not found.")
        return


    elif content.startswith("!ipwhois"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ipwhois" in TOOLS:
                result = TOOLS["ipwhois"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ipwhois` not found.")
        return


    elif content.startswith("!ip_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ip_api" in TOOLS:
                result = TOOLS["ip_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ip_api` not found.")
        return


    elif content.startswith("!jigsaw"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "jigsaw" in TOOLS:
                result = TOOLS["jigsaw"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `jigsaw` not found.")
        return


    elif content.startswith("!john_the_ripper"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "john_the_ripper" in TOOLS:
                result = TOOLS["john_the_ripper"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `john_the_ripper` not found.")
        return


    elif content.startswith("!kaldi"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "kaldi" in TOOLS:
                result = TOOLS["kaldi"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `kaldi` not found.")
        return


    elif content.startswith("!kibana"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "kibana" in TOOLS:
                result = TOOLS["kibana"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `kibana` not found.")
        return


    elif content.startswith("!knockpy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "knockpy" in TOOLS:
                result = TOOLS["knockpy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `knockpy` not found.")
        return


    elif content.startswith("!kubehunter"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "kubehunter" in TOOLS:
                result = TOOLS["kubehunter"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `kubehunter` not found.")
        return


    elif content.startswith("!langchain"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "langchain" in TOOLS:
                result = TOOLS["langchain"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `langchain` not found.")
        return


    elif content.startswith("!llamaindex"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "llamaindex" in TOOLS:
                result = TOOLS["llamaindex"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `llamaindex` not found.")
        return


    elif content.startswith("!llama_cpp"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "llama_cpp" in TOOLS:
                result = TOOLS["llama_cpp"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `llama_cpp` not found.")
        return


    elif content.startswith("!maltego"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "maltego" in TOOLS:
                result = TOOLS["maltego"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `maltego` not found.")
        return


    elif content.startswith("!maltego_ce"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "maltego_ce" in TOOLS:
                result = TOOLS["maltego_ce"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `maltego_ce` not found.")
        return


    elif content.startswith("!mapbox_geocoding_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "mapbox_geocoding_api" in TOOLS:
                result = TOOLS["mapbox_geocoding_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `mapbox_geocoding_api` not found.")
        return


    elif content.startswith("!masscan"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "masscan" in TOOLS:
                result = TOOLS["masscan"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `masscan` not found.")
        return


    elif content.startswith("!mastodon_py"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "mastodon_py" in TOOLS:
                result = TOOLS["mastodon_py"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `mastodon_py` not found.")
        return


    elif content.startswith("!medusa"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "medusa" in TOOLS:
                result = TOOLS["medusa"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `medusa` not found.")
        return


    elif content.startswith("!metagoofil"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "metagoofil" in TOOLS:
                result = TOOLS["metagoofil"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `metagoofil` not found.")
        return


    elif content.startswith("!metasploit"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "metasploit" in TOOLS:
                result = TOOLS["metasploit"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `metasploit` not found.")
        return


    elif content.startswith("!midjourney_cli"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "midjourney_cli" in TOOLS:
                result = TOOLS["midjourney_cli"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `midjourney_cli` not found.")
        return


    elif content.startswith("!misp"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "misp" in TOOLS:
                result = TOOLS["misp"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `misp` not found.")
        return


    elif content.startswith("!misp_push_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "misp_push_api" in TOOLS:
                result = TOOLS["misp_push_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `misp_push_api` not found.")
        return


    elif content.startswith("!mistral"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "mistral" in TOOLS:
                result = TOOLS["mistral"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `mistral` not found.")
        return


    elif content.startswith("!mobsf"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "mobsf" in TOOLS:
                result = TOOLS["mobsf"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `mobsf` not found.")
        return


    elif content.startswith("!mozilla_deepspeech"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "mozilla_deepspeech" in TOOLS:
                result = TOOLS["mozilla_deepspeech"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `mozilla_deepspeech` not found.")
        return


    elif content.startswith("!nessus_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "nessus_api" in TOOLS:
                result = TOOLS["nessus_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `nessus_api` not found.")
        return


    elif content.startswith("!netcraft"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "netcraft" in TOOLS:
                result = TOOLS["netcraft"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `netcraft` not found.")
        return


    elif content.startswith("!nikto"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "nikto" in TOOLS:
                result = TOOLS["nikto"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `nikto` not found.")
        return


    elif content.startswith("!nmap"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "nmap" in TOOLS:
                result = TOOLS["nmap"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `nmap` not found.")
        return


    elif content.startswith("!nordic_nrf_sniffer"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "nordic_nrf_sniffer" in TOOLS:
                result = TOOLS["nordic_nrf_sniffer"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `nordic_nrf_sniffer` not found.")
        return


    elif content.startswith("!ollama_tool"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ollama_tool" in TOOLS:
                result = TOOLS["ollama_tool"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ollama_tool` not found.")
        return


    elif content.startswith("!onionscan"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "onionscan" in TOOLS:
                result = TOOLS["onionscan"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `onionscan` not found.")
        return


    elif content.startswith("!onvif_device_manager"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "onvif_device_manager" in TOOLS:
                result = TOOLS["onvif_device_manager"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `onvif_device_manager` not found.")
        return


    elif content.startswith("!openai_dall_e"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openai_dall_e" in TOOLS:
                result = TOOLS["openai_dall_e"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openai_dall_e` not found.")
        return


    elif content.startswith("!openai_whisper"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openai_whisper" in TOOLS:
                result = TOOLS["openai_whisper"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openai_whisper` not found.")
        return


    elif content.startswith("!opendronemap"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "opendronemap" in TOOLS:
                result = TOOLS["opendronemap"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `opendronemap` not found.")
        return


    elif content.startswith("!openllm"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openllm" in TOOLS:
                result = TOOLS["openllm"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openllm` not found.")
        return


    elif content.startswith("!openlocks_database"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openlocks_database" in TOOLS:
                result = TOOLS["openlocks_database"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openlocks_database` not found.")
        return


    elif content.startswith("!openstreetmap_nominatim"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openstreetmap_nominatim" in TOOLS:
                result = TOOLS["openstreetmap_nominatim"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openstreetmap_nominatim` not found.")
        return


    elif content.startswith("!openvas"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openvas" in TOOLS:
                result = TOOLS["openvas"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openvas` not found.")
        return


    elif content.startswith("!openvpn_admin_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openvpn_admin_api" in TOOLS:
                result = TOOLS["openvpn_admin_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openvpn_admin_api` not found.")
        return


    elif content.startswith("!opt"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "opt" in TOOLS:
                result = TOOLS["opt"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `opt` not found.")
        return


    elif content.startswith("!osint_framework"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "osint_framework" in TOOLS:
                result = TOOLS["osint_framework"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `osint_framework` not found.")
        return


    elif content.startswith("!osmedeus"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "osmedeus" in TOOLS:
                result = TOOLS["osmedeus"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `osmedeus` not found.")
        return


    elif content.startswith("!otx_python_sdk"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "otx_python_sdk" in TOOLS:
                result = TOOLS["otx_python_sdk"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `otx_python_sdk` not found.")
        return


    elif content.startswith("!pdfminer_six"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "pdfminer_six" in TOOLS:
                result = TOOLS["pdfminer_six"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `pdfminer_six` not found.")
        return


    elif content.startswith("!peach_fuzzer"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "peach_fuzzer" in TOOLS:
                result = TOOLS["peach_fuzzer"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `peach_fuzzer` not found.")
        return


    elif content.startswith("!phantombuster"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "phantombuster" in TOOLS:
                result = TOOLS["phantombuster"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `phantombuster` not found.")
        return


    elif content.startswith("!photon"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "photon" in TOOLS:
                result = TOOLS["photon"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `photon` not found.")
        return


    elif content.startswith("!publicwww"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "publicwww" in TOOLS:
                result = TOOLS["publicwww"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `publicwww` not found.")
        return


    elif content.startswith("!pwntools"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "pwntools" in TOOLS:
                result = TOOLS["pwntools"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `pwntools` not found.")
        return


    elif content.startswith("!pythia"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "pythia" in TOOLS:
                result = TOOLS["pythia"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `pythia` not found.")
        return


    elif content.startswith("!qfield"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "qfield" in TOOLS:
                result = TOOLS["qfield"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `qfield` not found.")
        return


    elif content.startswith("!qgis_scripting"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "qgis_scripting" in TOOLS:
                result = TOOLS["qgis_scripting"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `qgis_scripting` not found.")
        return


    elif content.startswith("!quake"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "quake" in TOOLS:
                result = TOOLS["quake"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `quake` not found.")
        return


    elif content.startswith("!r2pipe"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "r2pipe" in TOOLS:
                result = TOOLS["r2pipe"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `r2pipe` not found.")
        return


    elif content.startswith("!radare2"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "radare2" in TOOLS:
                result = TOOLS["radare2"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `radare2` not found.")
        return


    elif content.startswith("!reaver"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "reaver" in TOOLS:
                result = TOOLS["reaver"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `reaver` not found.")
        return


    elif content.startswith("!recon_ng"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "recon_ng" in TOOLS:
                result = TOOLS["recon_ng"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `recon_ng` not found.")
        return


    elif content.startswith("!reddit_praw"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "reddit_praw" in TOOLS:
                result = TOOLS["reddit_praw"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `reddit_praw` not found.")
        return


    elif content.startswith("!riddler"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "riddler" in TOOLS:
                result = TOOLS["riddler"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `riddler` not found.")
        return


    elif content.startswith("!rtl_433"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "rtl_433" in TOOLS:
                result = TOOLS["rtl_433"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `rtl_433` not found.")
        return


    elif content.startswith("!rtsp_player"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "rtsp_player" in TOOLS:
                result = TOOLS["rtsp_player"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `rtsp_player` not found.")
        return


    elif content.startswith("!scapy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "scapy" in TOOLS:
                result = TOOLS["scapy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `scapy` not found.")
        return


    elif content.startswith("!shapely"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "shapely" in TOOLS:
                result = TOOLS["shapely"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `shapely` not found.")
        return


    elif content.startswith("!sherlock"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "sherlock" in TOOLS:
                result = TOOLS["sherlock"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `sherlock` not found.")
        return


    elif content.startswith("!sherlockly"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "sherlockly" in TOOLS:
                result = TOOLS["sherlockly"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `sherlockly` not found.")
        return


    elif content.startswith("!shodan"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "shodan" in TOOLS:
                result = TOOLS["shodan"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `shodan` not found.")
        return


    elif content.startswith("!sigstore"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "sigstore" in TOOLS:
                result = TOOLS["sigstore"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `sigstore` not found.")
        return


    elif content.startswith("!socialfish"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "socialfish" in TOOLS:
                result = TOOLS["socialfish"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `socialfish` not found.")
        return


    elif content.startswith("!social_engineer_toolkit_set"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "social_engineer_toolkit_set" in TOOLS:
                result = TOOLS["social_engineer_toolkit_set"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `social_engineer_toolkit_set` not found.")
        return


    elif content.startswith("!spiderfoot"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "spiderfoot" in TOOLS:
                result = TOOLS["spiderfoot"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `spiderfoot` not found.")
        return


    elif content.startswith("!sqlmap"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "sqlmap" in TOOLS:
                result = TOOLS["sqlmap"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `sqlmap` not found.")
        return


    elif content.startswith("!stable_diffusion"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "stable_diffusion" in TOOLS:
                result = TOOLS["stable_diffusion"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `stable_diffusion` not found.")
        return


    elif content.startswith("!subjack"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "subjack" in TOOLS:
                result = TOOLS["subjack"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `subjack` not found.")
        return


    elif content.startswith("!sublist3r"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "sublist3r" in TOOLS:
                result = TOOLS["sublist3r"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `sublist3r` not found.")
        return


    elif content.startswith("!tcpdump"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "tcpdump" in TOOLS:
                result = TOOLS["tcpdump"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `tcpdump` not found.")
        return


    elif content.startswith("!telegram_scraper"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "telegram_scraper" in TOOLS:
                result = TOOLS["telegram_scraper"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `telegram_scraper` not found.")
        return


    elif content.startswith("!tesseract_ocr"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "tesseract_ocr" in TOOLS:
                result = TOOLS["tesseract_ocr"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `tesseract_ocr` not found.")
        return


    elif content.startswith("!tineye_reverse_image_search"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "tineye_reverse_image_search" in TOOLS:
                result = TOOLS["tineye_reverse_image_search"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `tineye_reverse_image_search` not found.")
        return


    elif content.startswith("!tko_subs"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "tko_subs" in TOOLS:
                result = TOOLS["tko_subs"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `tko_subs` not found.")
        return


    elif content.startswith("!torbot"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "torbot" in TOOLS:
                result = TOOLS["torbot"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `torbot` not found.")
        return


    elif content.startswith("!trivy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "trivy" in TOOLS:
                result = TOOLS["trivy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `trivy` not found.")
        return


    elif content.startswith("!twint"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "twint" in TOOLS:
                result = TOOLS["twint"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `twint` not found.")
        return


    elif content.startswith("!urlcrazy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "urlcrazy" in TOOLS:
                result = TOOLS["urlcrazy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `urlcrazy` not found.")
        return


    elif content.startswith("!vhostscan"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "vhostscan" in TOOLS:
                result = TOOLS["vhostscan"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `vhostscan` not found.")
        return


    elif content.startswith("!virustotal_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "virustotal_api" in TOOLS:
                result = TOOLS["virustotal_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `virustotal_api` not found.")
        return


    elif content.startswith("!volatility"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "volatility" in TOOLS:
                result = TOOLS["volatility"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `volatility` not found.")
        return


    elif content.startswith("!wapiti"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "wapiti" in TOOLS:
                result = TOOLS["wapiti"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `wapiti` not found.")
        return


    elif content.startswith("!watchtower"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "watchtower" in TOOLS:
                result = TOOLS["watchtower"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `watchtower` not found.")
        return


    elif content.startswith("!wayback_machine"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "wayback_machine" in TOOLS:
                result = TOOLS["wayback_machine"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `wayback_machine` not found.")
        return


    elif content.startswith("!whois"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "whois" in TOOLS:
                result = TOOLS["whois"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `whois` not found.")
        return


    elif content.startswith("!wifi_pineapple_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "wifi_pineapple_api" in TOOLS:
                result = TOOLS["wifi_pineapple_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `wifi_pineapple_api` not found.")
        return


    elif content.startswith("!wigle"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "wigle" in TOOLS:
                result = TOOLS["wigle"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `wigle` not found.")
        return


    elif content.startswith("!wireshark"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "wireshark" in TOOLS:
                result = TOOLS["wireshark"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `wireshark` not found.")
        return


    elif content.startswith("!yandex_reverse_image_search"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "yandex_reverse_image_search" in TOOLS:
                result = TOOLS["yandex_reverse_image_search"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `yandex_reverse_image_search` not found.")
        return


    elif content.startswith("!yolov5"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "yolov5" in TOOLS:
                result = TOOLS["yolov5"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `yolov5` not found.")
        return


    elif content.startswith("!zap"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "zap" in TOOLS:
                result = TOOLS["zap"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `zap` not found.")
        return


    elif content.startswith("!zmap"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "zmap" in TOOLS:
                result = TOOLS["zmap"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `zmap` not found.")
        return


    elif content.startswith("!zoomeye"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "zoomeye" in TOOLS:
                result = TOOLS["zoomeye"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `zoomeye` not found.")
        return


--- Code snippets to add to Haunter Bot's on_message function: ---


    elif content.startswith("!4chan_api_client"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "4chan_api_client" in TOOLS:
                result = TOOLS["4chan_api_client"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `4chan_api_client` not found.")
        return


    elif content.startswith("!afl"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "afl" in TOOLS:
                result = TOOLS["afl"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `afl` not found.")
        return


    elif content.startswith("!ahmia"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ahmia" in TOOLS:
                result = TOOLS["ahmia"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ahmia` not found.")
        return


    elif content.startswith("!aircrack_ng"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "aircrack_ng" in TOOLS:
                result = TOOLS["aircrack_ng"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `aircrack_ng` not found.")
        return


    elif content.startswith("!alienvault_otx"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "alienvault_otx" in TOOLS:
                result = TOOLS["alienvault_otx"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `alienvault_otx` not found.")
        return


    elif content.startswith("!amass"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "amass" in TOOLS:
                result = TOOLS["amass"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `amass` not found.")
        return


    elif content.startswith("!anchore_engine"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "anchore_engine" in TOOLS:
                result = TOOLS["anchore_engine"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `anchore_engine` not found.")
        return


    elif content.startswith("!angelcam"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "angelcam" in TOOLS:
                result = TOOLS["angelcam"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `angelcam` not found.")
        return


    elif content.startswith("!apktool"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "apktool" in TOOLS:
                result = TOOLS["apktool"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `apktool` not found.")
        return


    elif content.startswith("!aquatone"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "aquatone" in TOOLS:
                result = TOOLS["aquatone"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `aquatone` not found.")
        return


    elif content.startswith("!assetfinder"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "assetfinder" in TOOLS:
                result = TOOLS["assetfinder"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `assetfinder` not found.")
        return


    elif content.startswith("!autopsy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "autopsy" in TOOLS:
                result = TOOLS["autopsy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `autopsy` not found.")
        return


    elif content.startswith("!aws_boto3"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "aws_boto3" in TOOLS:
                result = TOOLS["aws_boto3"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `aws_boto3` not found.")
        return


    elif content.startswith("!azure_sdk"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "azure_sdk" in TOOLS:
                result = TOOLS["azure_sdk"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `azure_sdk` not found.")
        return


    elif content.startswith("!beef"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "beef" in TOOLS:
                result = TOOLS["beef"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `beef` not found.")
        return


    elif content.startswith("!bettercap"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "bettercap" in TOOLS:
                result = TOOLS["bettercap"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `bettercap` not found.")
        return


    elif content.startswith("!binary_ninja"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "binary_ninja" in TOOLS:
                result = TOOLS["binary_ninja"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `binary_ninja` not found.")
        return


    elif content.startswith("!bing_image_search"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "bing_image_search" in TOOLS:
                result = TOOLS["bing_image_search"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `bing_image_search` not found.")
        return


    elif content.startswith("!bing_maps"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "bing_maps" in TOOLS:
                result = TOOLS["bing_maps"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `bing_maps` not found.")
        return


    elif content.startswith("!binwalk"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "binwalk" in TOOLS:
                result = TOOLS["binwalk"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `binwalk` not found.")
        return


    elif content.startswith("!blockchair_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "blockchair_api" in TOOLS:
                result = TOOLS["blockchair_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `blockchair_api` not found.")
        return


    elif content.startswith("!bloom"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "bloom" in TOOLS:
                result = TOOLS["bloom"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `bloom` not found.")
        return


    elif content.startswith("!bluez"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "bluez" in TOOLS:
                result = TOOLS["bluez"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `bluez` not found.")
        return


    elif content.startswith("!burp_suite"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "burp_suite" in TOOLS:
                result = TOOLS["burp_suite"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `burp_suite` not found.")
        return


    elif content.startswith("!bus_pirate"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "bus_pirate" in TOOLS:
                result = TOOLS["bus_pirate"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `bus_pirate` not found.")
        return


    elif content.startswith("!camstreamer"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "camstreamer" in TOOLS:
                result = TOOLS["camstreamer"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `camstreamer` not found.")
        return


    elif content.startswith("!censys"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "censys" in TOOLS:
                result = TOOLS["censys"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `censys` not found.")
        return


    elif content.startswith("!chainalysis_reactor"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "chainalysis_reactor" in TOOLS:
                result = TOOLS["chainalysis_reactor"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `chainalysis_reactor` not found.")
        return


    elif content.startswith("!chipwhisperer"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "chipwhisperer" in TOOLS:
                result = TOOLS["chipwhisperer"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `chipwhisperer` not found.")
        return


    elif content.startswith("!clearbit"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "clearbit" in TOOLS:
                result = TOOLS["clearbit"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `clearbit` not found.")
        return


    elif content.startswith("!cmu_sphinx"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "cmu_sphinx" in TOOLS:
                result = TOOLS["cmu_sphinx"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `cmu_sphinx` not found.")
        return


    elif content.startswith("!cobalt_strike"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "cobalt_strike" in TOOLS:
                result = TOOLS["cobalt_strike"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `cobalt_strike` not found.")
        return


    elif content.startswith("!cosign"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "cosign" in TOOLS:
                result = TOOLS["cosign"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `cosign` not found.")
        return


    elif content.startswith("!creepy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "creepy" in TOOLS:
                result = TOOLS["creepy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `creepy` not found.")
        return


    elif content.startswith("!cve_search"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "cve_search" in TOOLS:
                result = TOOLS["cve_search"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `cve_search` not found.")
        return


    elif content.startswith("!cyberchef"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "cyberchef" in TOOLS:
                result = TOOLS["cyberchef"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `cyberchef` not found.")
        return


    elif content.startswith("!datasploit"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "datasploit" in TOOLS:
                result = TOOLS["datasploit"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `datasploit` not found.")
        return


    elif content.startswith("!dehashed"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "dehashed" in TOOLS:
                result = TOOLS["dehashed"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `dehashed` not found.")
        return


    elif content.startswith("!dependency_track_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "dependency_track_api" in TOOLS:
                result = TOOLS["dependency_track_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `dependency_track_api` not found.")
        return


    elif content.startswith("!dnsdumpster"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "dnsdumpster" in TOOLS:
                result = TOOLS["dnsdumpster"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `dnsdumpster` not found.")
        return


    elif content.startswith("!duckduckgo_images"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "duckduckgo_images" in TOOLS:
                result = TOOLS["duckduckgo_images"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `duckduckgo_images` not found.")
        return


    elif content.startswith("!elasticsearch"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "elasticsearch" in TOOLS:
                result = TOOLS["elasticsearch"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `elasticsearch` not found.")
        return


    elif content.startswith("!eleutherai_gpt_neo"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "eleutherai_gpt_neo" in TOOLS:
                result = TOOLS["eleutherai_gpt_neo"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `eleutherai_gpt_neo` not found.")
        return


    elif content.startswith("!eleutherai_gpt_neox"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "eleutherai_gpt_neox" in TOOLS:
                result = TOOLS["eleutherai_gpt_neox"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `eleutherai_gpt_neox` not found.")
        return


    elif content.startswith("!emailrep"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "emailrep" in TOOLS:
                result = TOOLS["emailrep"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `emailrep` not found.")
        return


    elif content.startswith("!esptool"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "esptool" in TOOLS:
                result = TOOLS["esptool"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `esptool` not found.")
        return


    elif content.startswith("!etherscan_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "etherscan_api" in TOOLS:
                result = TOOLS["etherscan_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `etherscan_api` not found.")
        return


    elif content.startswith("!exiftool"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "exiftool" in TOOLS:
                result = TOOLS["exiftool"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `exiftool` not found.")
        return


    elif content.startswith("!eyewitness"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "eyewitness" in TOOLS:
                result = TOOLS["eyewitness"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `eyewitness` not found.")
        return


    elif content.startswith("!face_recognition"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "face_recognition" in TOOLS:
                result = TOOLS["face_recognition"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `face_recognition` not found.")
        return


    elif content.startswith("!falcon"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "falcon" in TOOLS:
                result = TOOLS["falcon"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `falcon` not found.")
        return


    elif content.startswith("!flan_t5"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "flan_t5" in TOOLS:
                result = TOOLS["flan_t5"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `flan_t5` not found.")
        return


    elif content.startswith("!foca"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "foca" in TOOLS:
                result = TOOLS["foca"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `foca` not found.")
        return


    elif content.startswith("!frida"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "frida" in TOOLS:
                result = TOOLS["frida"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `frida` not found.")
        return


    elif content.startswith("!ftk_imager"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ftk_imager" in TOOLS:
                result = TOOLS["ftk_imager"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ftk_imager` not found.")
        return


    elif content.startswith("!gcp_sdk"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "gcp_sdk" in TOOLS:
                result = TOOLS["gcp_sdk"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `gcp_sdk` not found.")
        return


    elif content.startswith("!geoip2"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "geoip2" in TOOLS:
                result = TOOLS["geoip2"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `geoip2` not found.")
        return


    elif content.startswith("!geopy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "geopy" in TOOLS:
                result = TOOLS["geopy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `geopy` not found.")
        return


    elif content.startswith("!ghidra"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ghidra" in TOOLS:
                result = TOOLS["ghidra"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ghidra` not found.")
        return


    elif content.startswith("!ghunt"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ghunt" in TOOLS:
                result = TOOLS["ghunt"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ghunt` not found.")
        return


    elif content.startswith("!github_archive_spark"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "github_archive_spark" in TOOLS:
                result = TOOLS["github_archive_spark"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `github_archive_spark` not found.")
        return


    elif content.startswith("!gitleaks"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "gitleaks" in TOOLS:
                result = TOOLS["gitleaks"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `gitleaks` not found.")
        return


    elif content.startswith("!gnu_radio"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "gnu_radio" in TOOLS:
                result = TOOLS["gnu_radio"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `gnu_radio` not found.")
        return


    elif content.startswith("!google_geofencing_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "google_geofencing_api" in TOOLS:
                result = TOOLS["google_geofencing_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `google_geofencing_api` not found.")
        return


    elif content.startswith("!google_images_search"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "google_images_search" in TOOLS:
                result = TOOLS["google_images_search"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `google_images_search` not found.")
        return


    elif content.startswith("!google_speech_to_text"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "google_speech_to_text" in TOOLS:
                result = TOOLS["google_speech_to_text"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `google_speech_to_text` not found.")
        return


    elif content.startswith("!gophish"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "gophish" in TOOLS:
                result = TOOLS["gophish"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `gophish` not found.")
        return


    elif content.startswith("!gpt4all"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "gpt4all" in TOOLS:
                result = TOOLS["gpt4all"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `gpt4all` not found.")
        return


    elif content.startswith("!gpt_j"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "gpt_j" in TOOLS:
                result = TOOLS["gpt_j"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `gpt_j` not found.")
        return


    elif content.startswith("!greenbone_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "greenbone_api" in TOOLS:
                result = TOOLS["greenbone_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `greenbone_api` not found.")
        return


    elif content.startswith("!greyhat_warfare"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "greyhat_warfare" in TOOLS:
                result = TOOLS["greyhat_warfare"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `greyhat_warfare` not found.")
        return


    elif content.startswith("!harvester"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "harvester" in TOOLS:
                result = TOOLS["harvester"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `harvester` not found.")
        return


    elif content.startswith("!hashcat"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "hashcat" in TOOLS:
                result = TOOLS["hashcat"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `hashcat` not found.")
        return


    elif content.startswith("!hash_identifier"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "hash_identifier" in TOOLS:
                result = TOOLS["hash_identifier"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `hash_identifier` not found.")
        return


    elif content.startswith("!have_i_been_pwned"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "have_i_been_pwned" in TOOLS:
                result = TOOLS["have_i_been_pwned"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `have_i_been_pwned` not found.")
        return


    elif content.startswith("!hugging_face_transformers"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "hugging_face_transformers" in TOOLS:
                result = TOOLS["hugging_face_transformers"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `hugging_face_transformers` not found.")
        return


    elif content.startswith("!hunter_io"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "hunter_io" in TOOLS:
                result = TOOLS["hunter_io"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `hunter_io` not found.")
        return


    elif content.startswith("!hydra"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "hydra" in TOOLS:
                result = TOOLS["hydra"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `hydra` not found.")
        return


    elif content.startswith("!insecam"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "insecam" in TOOLS:
                result = TOOLS["insecam"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `insecam` not found.")
        return


    elif content.startswith("!inspy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "inspy" in TOOLS:
                result = TOOLS["inspy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `inspy` not found.")
        return


    elif content.startswith("!inteltechniques_tools"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "inteltechniques_tools" in TOOLS:
                result = TOOLS["inteltechniques_tools"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `inteltechniques_tools` not found.")
        return


    elif content.startswith("!ipify"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ipify" in TOOLS:
                result = TOOLS["ipify"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ipify` not found.")
        return


    elif content.startswith("!ipinfo"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ipinfo" in TOOLS:
                result = TOOLS["ipinfo"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ipinfo` not found.")
        return


    elif content.startswith("!ipwhois"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ipwhois" in TOOLS:
                result = TOOLS["ipwhois"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ipwhois` not found.")
        return


    elif content.startswith("!ip_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ip_api" in TOOLS:
                result = TOOLS["ip_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ip_api` not found.")
        return


    elif content.startswith("!jigsaw"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "jigsaw" in TOOLS:
                result = TOOLS["jigsaw"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `jigsaw` not found.")
        return


    elif content.startswith("!john_the_ripper"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "john_the_ripper" in TOOLS:
                result = TOOLS["john_the_ripper"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `john_the_ripper` not found.")
        return


    elif content.startswith("!kaldi"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "kaldi" in TOOLS:
                result = TOOLS["kaldi"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `kaldi` not found.")
        return


    elif content.startswith("!kibana"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "kibana" in TOOLS:
                result = TOOLS["kibana"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `kibana` not found.")
        return


    elif content.startswith("!knockpy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "knockpy" in TOOLS:
                result = TOOLS["knockpy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `knockpy` not found.")
        return


    elif content.startswith("!kubehunter"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "kubehunter" in TOOLS:
                result = TOOLS["kubehunter"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `kubehunter` not found.")
        return


    elif content.startswith("!langchain"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "langchain" in TOOLS:
                result = TOOLS["langchain"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `langchain` not found.")
        return


    elif content.startswith("!llamaindex"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "llamaindex" in TOOLS:
                result = TOOLS["llamaindex"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `llamaindex` not found.")
        return


    elif content.startswith("!llama_cpp"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "llama_cpp" in TOOLS:
                result = TOOLS["llama_cpp"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `llama_cpp` not found.")
        return


    elif content.startswith("!maltego"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "maltego" in TOOLS:
                result = TOOLS["maltego"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `maltego` not found.")
        return


    elif content.startswith("!maltego_ce"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "maltego_ce" in TOOLS:
                result = TOOLS["maltego_ce"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `maltego_ce` not found.")
        return


    elif content.startswith("!mapbox_geocoding_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "mapbox_geocoding_api" in TOOLS:
                result = TOOLS["mapbox_geocoding_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `mapbox_geocoding_api` not found.")
        return


    elif content.startswith("!masscan"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "masscan" in TOOLS:
                result = TOOLS["masscan"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `masscan` not found.")
        return


    elif content.startswith("!mastodon_py"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "mastodon_py" in TOOLS:
                result = TOOLS["mastodon_py"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `mastodon_py` not found.")
        return


    elif content.startswith("!medusa"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "medusa" in TOOLS:
                result = TOOLS["medusa"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `medusa` not found.")
        return


    elif content.startswith("!metagoofil"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "metagoofil" in TOOLS:
                result = TOOLS["metagoofil"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `metagoofil` not found.")
        return


    elif content.startswith("!metasploit"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "metasploit" in TOOLS:
                result = TOOLS["metasploit"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `metasploit` not found.")
        return


    elif content.startswith("!midjourney_cli"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "midjourney_cli" in TOOLS:
                result = TOOLS["midjourney_cli"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `midjourney_cli` not found.")
        return


    elif content.startswith("!misp"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "misp" in TOOLS:
                result = TOOLS["misp"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `misp` not found.")
        return


    elif content.startswith("!misp_push_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "misp_push_api" in TOOLS:
                result = TOOLS["misp_push_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `misp_push_api` not found.")
        return


    elif content.startswith("!mistral"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "mistral" in TOOLS:
                result = TOOLS["mistral"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `mistral` not found.")
        return


    elif content.startswith("!mobsf"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "mobsf" in TOOLS:
                result = TOOLS["mobsf"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `mobsf` not found.")
        return


    elif content.startswith("!mozilla_deepspeech"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "mozilla_deepspeech" in TOOLS:
                result = TOOLS["mozilla_deepspeech"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `mozilla_deepspeech` not found.")
        return


    elif content.startswith("!nessus_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "nessus_api" in TOOLS:
                result = TOOLS["nessus_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `nessus_api` not found.")
        return


    elif content.startswith("!netcraft"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "netcraft" in TOOLS:
                result = TOOLS["netcraft"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `netcraft` not found.")
        return


    elif content.startswith("!nikto"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "nikto" in TOOLS:
                result = TOOLS["nikto"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `nikto` not found.")
        return


    elif content.startswith("!nmap"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "nmap" in TOOLS:
                result = TOOLS["nmap"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `nmap` not found.")
        return


    elif content.startswith("!nordic_nrf_sniffer"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "nordic_nrf_sniffer" in TOOLS:
                result = TOOLS["nordic_nrf_sniffer"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `nordic_nrf_sniffer` not found.")
        return


    elif content.startswith("!ollama_tool"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "ollama_tool" in TOOLS:
                result = TOOLS["ollama_tool"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `ollama_tool` not found.")
        return


    elif content.startswith("!onionscan"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "onionscan" in TOOLS:
                result = TOOLS["onionscan"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `onionscan` not found.")
        return


    elif content.startswith("!onvif_device_manager"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "onvif_device_manager" in TOOLS:
                result = TOOLS["onvif_device_manager"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `onvif_device_manager` not found.")
        return


    elif content.startswith("!openai_dall_e"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openai_dall_e" in TOOLS:
                result = TOOLS["openai_dall_e"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openai_dall_e` not found.")
        return


    elif content.startswith("!openai_whisper"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openai_whisper" in TOOLS:
                result = TOOLS["openai_whisper"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openai_whisper` not found.")
        return


    elif content.startswith("!opendronemap"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "opendronemap" in TOOLS:
                result = TOOLS["opendronemap"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `opendronemap` not found.")
        return


    elif content.startswith("!openllm"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openllm" in TOOLS:
                result = TOOLS["openllm"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openllm` not found.")
        return


    elif content.startswith("!openlocks_database"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openlocks_database" in TOOLS:
                result = TOOLS["openlocks_database"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openlocks_database` not found.")
        return


    elif content.startswith("!openstreetmap_nominatim"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openstreetmap_nominatim" in TOOLS:
                result = TOOLS["openstreetmap_nominatim"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openstreetmap_nominatim` not found.")
        return


    elif content.startswith("!openvas"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openvas" in TOOLS:
                result = TOOLS["openvas"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openvas` not found.")
        return


    elif content.startswith("!openvpn_admin_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "openvpn_admin_api" in TOOLS:
                result = TOOLS["openvpn_admin_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `openvpn_admin_api` not found.")
        return


    elif content.startswith("!opt"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "opt" in TOOLS:
                result = TOOLS["opt"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `opt` not found.")
        return


    elif content.startswith("!osint_framework"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "osint_framework" in TOOLS:
                result = TOOLS["osint_framework"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `osint_framework` not found.")
        return


    elif content.startswith("!osmedeus"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "osmedeus" in TOOLS:
                result = TOOLS["osmedeus"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `osmedeus` not found.")
        return


    elif content.startswith("!otx_python_sdk"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "otx_python_sdk" in TOOLS:
                result = TOOLS["otx_python_sdk"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `otx_python_sdk` not found.")
        return


    elif content.startswith("!pdfminer_six"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "pdfminer_six" in TOOLS:
                result = TOOLS["pdfminer_six"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `pdfminer_six` not found.")
        return


    elif content.startswith("!peach_fuzzer"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "peach_fuzzer" in TOOLS:
                result = TOOLS["peach_fuzzer"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `peach_fuzzer` not found.")
        return


    elif content.startswith("!phantombuster"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "phantombuster" in TOOLS:
                result = TOOLS["phantombuster"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `phantombuster` not found.")
        return


    elif content.startswith("!photon"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "photon" in TOOLS:
                result = TOOLS["photon"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `photon` not found.")
        return


    elif content.startswith("!publicwww"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "publicwww" in TOOLS:
                result = TOOLS["publicwww"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `publicwww` not found.")
        return


    elif content.startswith("!pwntools"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "pwntools" in TOOLS:
                result = TOOLS["pwntools"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `pwntools` not found.")
        return


    elif content.startswith("!pythia"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "pythia" in TOOLS:
                result = TOOLS["pythia"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `pythia` not found.")
        return


    elif content.startswith("!qfield"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "qfield" in TOOLS:
                result = TOOLS["qfield"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `qfield` not found.")
        return


    elif content.startswith("!qgis_scripting"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "qgis_scripting" in TOOLS:
                result = TOOLS["qgis_scripting"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `qgis_scripting` not found.")
        return


    elif content.startswith("!quake"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "quake" in TOOLS:
                result = TOOLS["quake"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `quake` not found.")
        return


    elif content.startswith("!r2pipe"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "r2pipe" in TOOLS:
                result = TOOLS["r2pipe"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `r2pipe` not found.")
        return


    elif content.startswith("!radare2"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "radare2" in TOOLS:
                result = TOOLS["radare2"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `radare2` not found.")
        return


    elif content.startswith("!reaver"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "reaver" in TOOLS:
                result = TOOLS["reaver"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `reaver` not found.")
        return


    elif content.startswith("!recon_ng"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "recon_ng" in TOOLS:
                result = TOOLS["recon_ng"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `recon_ng` not found.")
        return


    elif content.startswith("!reddit_praw"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "reddit_praw" in TOOLS:
                result = TOOLS["reddit_praw"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `reddit_praw` not found.")
        return


    elif content.startswith("!riddler"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "riddler" in TOOLS:
                result = TOOLS["riddler"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `riddler` not found.")
        return


    elif content.startswith("!rtl_433"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "rtl_433" in TOOLS:
                result = TOOLS["rtl_433"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `rtl_433` not found.")
        return


    elif content.startswith("!rtsp_player"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "rtsp_player" in TOOLS:
                result = TOOLS["rtsp_player"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `rtsp_player` not found.")
        return


    elif content.startswith("!scapy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "scapy" in TOOLS:
                result = TOOLS["scapy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `scapy` not found.")
        return


    elif content.startswith("!shapely"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "shapely" in TOOLS:
                result = TOOLS["shapely"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `shapely` not found.")
        return


    elif content.startswith("!sherlock"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "sherlock" in TOOLS:
                result = TOOLS["sherlock"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `sherlock` not found.")
        return


    elif content.startswith("!sherlockly"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "sherlockly" in TOOLS:
                result = TOOLS["sherlockly"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `sherlockly` not found.")
        return


    elif content.startswith("!shodan"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "shodan" in TOOLS:
                result = TOOLS["shodan"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `shodan` not found.")
        return


    elif content.startswith("!sigstore"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "sigstore" in TOOLS:
                result = TOOLS["sigstore"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `sigstore` not found.")
        return


    elif content.startswith("!socialfish"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "socialfish" in TOOLS:
                result = TOOLS["socialfish"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `socialfish` not found.")
        return


    elif content.startswith("!social_engineer_toolkit_set"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "social_engineer_toolkit_set" in TOOLS:
                result = TOOLS["social_engineer_toolkit_set"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `social_engineer_toolkit_set` not found.")
        return


    elif content.startswith("!spiderfoot"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "spiderfoot" in TOOLS:
                result = TOOLS["spiderfoot"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `spiderfoot` not found.")
        return


    elif content.startswith("!sqlmap"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "sqlmap" in TOOLS:
                result = TOOLS["sqlmap"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `sqlmap` not found.")
        return


    elif content.startswith("!stable_diffusion"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "stable_diffusion" in TOOLS:
                result = TOOLS["stable_diffusion"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `stable_diffusion` not found.")
        return


    elif content.startswith("!subjack"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "subjack" in TOOLS:
                result = TOOLS["subjack"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `subjack` not found.")
        return


    elif content.startswith("!sublist3r"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "sublist3r" in TOOLS:
                result = TOOLS["sublist3r"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `sublist3r` not found.")
        return


    elif content.startswith("!tcpdump"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "tcpdump" in TOOLS:
                result = TOOLS["tcpdump"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `tcpdump` not found.")
        return


    elif content.startswith("!telegram_scraper"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "telegram_scraper" in TOOLS:
                result = TOOLS["telegram_scraper"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `telegram_scraper` not found.")
        return


    elif content.startswith("!tesseract_ocr"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "tesseract_ocr" in TOOLS:
                result = TOOLS["tesseract_ocr"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `tesseract_ocr` not found.")
        return


    elif content.startswith("!tineye_reverse_image_search"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "tineye_reverse_image_search" in TOOLS:
                result = TOOLS["tineye_reverse_image_search"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `tineye_reverse_image_search` not found.")
        return


    elif content.startswith("!tko_subs"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "tko_subs" in TOOLS:
                result = TOOLS["tko_subs"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `tko_subs` not found.")
        return


    elif content.startswith("!torbot"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "torbot" in TOOLS:
                result = TOOLS["torbot"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `torbot` not found.")
        return


    elif content.startswith("!trivy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "trivy" in TOOLS:
                result = TOOLS["trivy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `trivy` not found.")
        return


    elif content.startswith("!twint"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "twint" in TOOLS:
                result = TOOLS["twint"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `twint` not found.")
        return


    elif content.startswith("!urlcrazy"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "urlcrazy" in TOOLS:
                result = TOOLS["urlcrazy"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `urlcrazy` not found.")
        return


    elif content.startswith("!vhostscan"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "vhostscan" in TOOLS:
                result = TOOLS["vhostscan"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `vhostscan` not found.")
        return


    elif content.startswith("!virustotal_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "virustotal_api" in TOOLS:
                result = TOOLS["virustotal_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `virustotal_api` not found.")
        return


    elif content.startswith("!volatility"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "volatility" in TOOLS:
                result = TOOLS["volatility"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `volatility` not found.")
        return


    elif content.startswith("!wapiti"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "wapiti" in TOOLS:
                result = TOOLS["wapiti"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `wapiti` not found.")
        return


    elif content.startswith("!watchtower"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "watchtower" in TOOLS:
                result = TOOLS["watchtower"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `watchtower` not found.")
        return


    elif content.startswith("!wayback_machine"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "wayback_machine" in TOOLS:
                result = TOOLS["wayback_machine"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `wayback_machine` not found.")
        return


    elif content.startswith("!whois"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "whois" in TOOLS:
                result = TOOLS["whois"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `whois` not found.")
        return


    elif content.startswith("!wifi_pineapple_api"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "wifi_pineapple_api" in TOOLS:
                result = TOOLS["wifi_pineapple_api"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `wifi_pineapple_api` not found.")
        return


    elif content.startswith("!wigle"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "wigle" in TOOLS:
                result = TOOLS["wigle"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `wigle` not found.")
        return


    elif content.startswith("!wireshark"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "wireshark" in TOOLS:
                result = TOOLS["wireshark"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `wireshark` not found.")
        return


    elif content.startswith("!yandex_reverse_image_search"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "yandex_reverse_image_search" in TOOLS:
                result = TOOLS["yandex_reverse_image_search"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `yandex_reverse_image_search` not found.")
        return


    elif content.startswith("!yolov5"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "yolov5" in TOOLS:
                result = TOOLS["yolov5"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `yolov5` not found.")
        return


    elif content.startswith("!zap"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "zap" in TOOLS:
                result = TOOLS["zap"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `zap` not found.")
        return


    elif content.startswith("!zmap"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "zmap" in TOOLS:
                result = TOOLS["zmap"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `zmap` not found.")
        return


    elif content.startswith("!zoomeye"):
        _, *arg_parts = content.split(" ", 1)
        arg = arg_parts[0] if arg_parts else ""
        async with message.channel.typing():
            if "zoomeye" in TOOLS:
                result = TOOLS["zoomeye"](arg)
                for part in chunk(f""""{result}""""):
                    await message.channel.send(part)
            else:
                await message.channel.send("Tool `zoomeye` not found.")
        return

PS F:\Projects\haun>
