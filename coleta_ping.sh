#!/bin/bash


if [ -z "$1" ]; then
  echo "Uso: $0 <ROTULO>"
  exit 1
fi

ROTULO=$1
ARQUIVO="dados_ping.csv"

if [ ! -f "$ARQUIVO" ]; then
  echo "rotulo,seq,tempo_ms" > "$ARQUIVO"
fi

echo "Iniciando coleta de 100 pings para www.ufs.br com rótulo '$ROTULO'..."
ping -c 100 www.ufs.br | while read LINHA; do
  echo "$LINHA"

  if [[ $LINHA == *"time="* ]]; then
    SEQ=$(echo $LINHA | sed -n 's/.*icmp_seq=\([0-9]\+\).*/\1/p')
    TEMPO=$(echo $LINHA | sed -n 's/.*time=\([0-9.]\+\).*/\1/p')

    if [ -n "$SEQ" ] && [ -n "$TEMPO" ]; then
      echo "$ROTULO,$SEQ,$TEMPO" >> "$ARQUIVO"
    fi
  fi
done

echo "Coleta concluída. Dados adicionados em $ARQUIVO"