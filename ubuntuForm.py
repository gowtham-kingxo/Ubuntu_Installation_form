from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("profile.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
     # result = str(request.form["hostname"])
      hostname = str(request.form["hostname"])
      user_name = str(request.form["user_name"])
      pw = str(request.form["ps"])
      full_name = str(request.form["full_name"])
      confirm_pw = str(request.form["confirm_pw"])
      # lang   = str(request.form["lang"])
      # location = str(request.form["location"])
      # time_zone = str(request.form["time_zone"])
      # proxy = str(request.form["proxy"])
      # partition = str(request.form["partition"])


      preseed =""" ### Localization
            d-i debian-installer/locale string en_US
            d-i console-setup/ask_detect boolean false
            d-i keyboard-configuration/layoutcode string us
            
            ### Network configuration
            d-i netcfg/choose_interface select auto
            d-i netcfg/get_hostname string """+hostname+"""
            d-i netcfg/get_domain string unassigned-domain
            d-i netcfg/wireless_wep string
            
            ### Mirror settings
            #d-i mirror/http/countries select US
            #d-i mirror/country string US
            #d-i mirror/http/hostname string us.archive.ubuntu.com
            #d-i mirror/http/directory string /images/Ubuntu/16.04
            #d-i mirror/http/mirror select us.archive.ubuntu.com
            #d-i mirror/http/proxy string
            
            ### Clock and time zone setup
            d-i clock-setup/utc boolean true
            d-i time/zone string Asia/Calcutta
            d-i clock-setup/ntp boolean true
            
            ### Partitioning
            #d-i partman-auto/disk string /dev/vda
            #d-i partman-auto/method string lvm
            #d-i partman-lvm/device_remove_lvm boolean true
            #d-i partman-md/device_remove_md boolean true
            #d-i partman-lvm/confirm boolean false
            #d-i partman-lvm/confirm_nooverwrite boolean true
            #d-i partman-auto-lvm/guided_size string max
            ## - atomic: all files in one partition
            ## - home:   separate /home partition
            ## - multi:  separate /home, /usr, /var, and /tmp partitions
            #d-i partman-auto/choose_recipe select atomic
            #d-i partman-partitioning/confirm_write_new_label boolean true
            #d-i partman/choose_partition select finish
            #d-i partman/confirm boolean true
            #d-i partman/confirm_nooverwrite boolean true
            #d-i partman-md/confirm boolean true
            #d-i partman-partitioning/confirm_write_new_label boolean true
            #d-i partman/choose_partition select finish
            #d-i partman/confirm_nooverwrite boolean true
            
            
            
            
            
            
            
            ### Account setup
            d-i passwd/root-login boolean false
            d-i passwd/user-fullname string """+full_name+"""
            d-i passwd/username string """+user_name+"""
            d-i passwd/user-password password """+pw+"""
            d-i passwd/user-password-again password """+pw+"""
            # Use mkpasswd -m sha-512 to create an MD5 hash password
            #d-i passwd/user-password-crypted password [MD5 hash]
            d-i user-setup/allow-password-weak boolean true
            d-i user-setup/encrypt-home boolean false
            
            ### Apt setup
            
            ### Package selection
            tasksel tasksel/first multiselect
            # Individual additional packages to install
            d-i pkgsel/include string git openssh-server python-simplejson sudo
            d-i pkgsel/update-policy select none
            d-i pkgsel/upgrade select none
            popularity-contest popularity-contest/participate boolean false
            
            ### Boot loader installation
            d-i grub-installer/only_debian boolean true
            d-i grub-installer/with_other_os boolean true
            
            ### Finishing up the installation
            d-i finish-install/reboot_in_progress note
            d-i debian-installer/exit/poweroff boolean true
            
            ### Preseeding other packages
            
            #### Advanced options
            #d-i preseed/late_command string \
            #echo "ubuntu    ALL=(ALL) NOPASSWD:ALL" >> /target/etc/sudoers; \
            #in-target ln -s /lib/systemd/system/serial-getty@.service /etc/systemd/system/getty.target.wants/serial-getty@ttyS0.service; \
            #rm -f /target/etc/ssh/ssh_host_*; \
            #in-target sed -i -e 's|exit 0||' /etc/rc.local; \
            #in-target sed -i -e 's|.*test -f /etc/ssh/ssh_host_dsa_key.*||' /etc/rc.local; \
            #in-target bash -c 'echo "test -f /etc/ssh/ssh_host_dsa_key || dpkg-reconfigure openssh-server" >> /etc/rc.local'; \
            #in-target bash -c 'echo "exit 0" >> /etc/rc.local'; \
            #cat /dev/null > /target/etc/hostname"""



      if (pw == confirm_pw):
            print(hostname)
            f = open("preseed23.cfg", "w+")
            f.write(preseed)
            return render_template("result.html", result=hostname+pw+" "+full_name+" "+confirm_pw)
      else:
          error = "wrong password"
          return render_template("profile.html", error=error )



if __name__=="__main__":
    app.debug = True
    app.run()
    app.run(debug=True)