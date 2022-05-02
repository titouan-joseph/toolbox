# Monitoring d'interface

Pour copier le trafic d'une interface vers une autre pour du monitoring. Pratique pour des observation avec wireshark

Tout ce fait en mode de configuration global  

```cisco
enable
configure terminal
```

## Envoyer le trafic vers un interface

```cisco
monitor session 1 destination interface [interface name]
```

## Selectionner le trafic a envoyé

### Depuis un vlan

```cisco
monitor session 1 source vlan [vlan ID]
```

### Depuis une interface

```cisco
monitor session 1 source interface [interface name]
```
