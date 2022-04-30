#!/bin/sh

# On vide les règles déjà existantes
iptables -t filter -F
iptables -t filter -X

# On refuse toutes les connexions
iptables -t filter -P INPUT DROP
iptables -t filter -P FORWARD DROP
iptables -t filter -P OUTPUT DROP
echo "On interdit tout"

# On autorise les connexions déjà établie
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT
echo "On autorise les connexiosn déjà établie"

# On autorise le loop-back (localhost)
iptables -t filter -A INPUT -i lo -j ACCEPT --comment "Accept loopback"
iptables -t filter -A OUTPUT -o lo -j ACCEPT --comment "Accept loopback"
echo "On authorise loopback"

# On autorise le SSH (à adapter suivant votre cas)
iptables -t filter -A INPUT -p tcp --dport 22 -j ACCEPT --comment "Accept SSH port"
iptables -t filter -A OUTPUT -p tcp --dport 22 -j ACCEPT --comment "Accept SSH port"
echo "Autorise SSH"

# HTTP
iptables -t filter -A OUTPUT -p tcp --dport 80 -j ACCEPT --comment "Accept HTTP"
iptables -t filter -A OUTPUT -p tcp --dport 443 -j ACCEPT --comment "Accep HTTPS"
iptables -t filter -A INPUT -p tcp --dport 80 -j ACCEPT --comment "Accept HTTP"
iptables -t filter -A INPUT -p tcp --dport 443 -j ACCEPT --comment "Accep HTTPS"
echo "Autorise HTTP et HTTPS"
