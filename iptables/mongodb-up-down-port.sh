case $1 in
	"--up"|"-u")
		sudo iptables -t filter -A INPUT -p tcp --dport 27017 -j ACCEPT --comment "Accept mongodb port"
  		sudo iptables -t filter -A OUTPUT -p tcp --dport 27017 -j ACCEPT --comment "Accept mongodb port"
		;;
	"--down"|"-d")
		sudo iptables -D INPUT -p tcp --dport 27017 -j ACCEPT
		sudo iptables -D OUTPUT -p tcp --dport 27017 -j ACCEPT
		;;
esac
