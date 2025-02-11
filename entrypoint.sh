#!/bin/bash

#ห้ามลบ cleanup มิฉะนั้นจะเกิดกระบวนการซอมบี้
function cleanup()
{
    local pids=`jobs -p`
    if [[ "${pids}" != ""  ]]; then
        kill ${pids} >/dev/null 2>/dev/null
    fi
}

action="${1-start}"
service="${2-all}"

trap cleanup EXIT

rm -f /opt/jumpserver/tmp/*.pid

if [[ "$action" == "bash" || "$action" == "sh" ]];then
    bash
elif [[ "$action" == "sleep" ]];then
    echo "Sleep 365 days"
    sleep 365d
else
    which cron &>/dev/null && [[ ! -f /var/run/crond.pid ]] && cron || echo ""
    python jms "${action}" "${service}"
fi
