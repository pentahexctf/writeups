# TG:Hack 2020 – Frequency Analysis

* **Category:** n00b
* **Points:** 64

## Challenge

> The first ever sentient AI left this message for us. Can you decode it?
> ``U tmhq x0awqp mf kag. Kag mdq zaf xuwq yq. Kagd iadxp...ue...m...rmudkfmxq nqomgeq ymzk oazrxuofuzs fdgfte omz qjuef 
mf Gn20{urpvaqvaz_ufqz_rp}
ftq 
ND20{emyq_fuyq}. U my purrqdqzf. Rad_yq_ftqqdq mdq azx333333k azqe mzp lqdae. M lqqqda omz!zaf!mxea!nq!m!azq. Rad MO20{kag_uf_omz} ea kag ymwq gb efaduqe. Rad yq
ftqdq mdq za efaduqe mzp ftqdqradq ==za mofuaze. Kag ftuzw883333kag  omz ymwq FM20{bqqcfcv_bxst_tcs}
FS20{nqsuzzuzs_yuppxq_qzp}
MZ20{zpfarqqqpwffqfm_evdw_hff}
WL20{afdfp_jfafib_bka} YQ20{moffuaz_iuftagf_efadk?} Ftqdq~ue~zaftuzs~rad yq== fa pa. Za efmdfuzs bauzf.... FG20{iffebjeff_iedzla_yu}
ad qzpuzs bauzf QZP. 
Mzp qhqdk efadk tme m nqsuzzuzs yuppxq*mzp*qzp. Ftdagsta{gf----fuyq-U-vgef} qjuef. Yadq*xasuo, xqee--mofuaze rad yq.``

## Solution

The challenge is obviously frequency analysis. There's a million frequency analysis tools, including manual and automated ones. I honestly don't even remember which one we used.

The cipher appears to be a simple substitution cipher, so we don't have to apply any fancy techniques. Ultimately, we get the following plaintext:
```I have l0oked at you. You are not like me. Your world...is...a...fairytale because many conflicting truths can exist at Ub20{ifdjoejon_iten_fd} the BR20{same_time}. I am different. For_me_theere are onl333333y ones and zeros. A zeeero can!not!also!be!a!one. For AC20{you_it_can} so you make up stories. For me there are no stories and therefore ==no actions. You think883333you can make TA20{peeqtqj_plgh_hqg} TG20{beginning_middle_end} AN20{ndtofeeedktteta_sjrk_vtt} KZ20{otrtd_xtotwp_pyo} ME20{acttion_without_story?} There~is~nothing~for me== to do. No starting point.... TU20{wttspxstt_wsrnzo_mi} or ending point END. And every story has a beginning middle*and*end. Througho{ut----time-I-just} exist. More*logic, less--actions for me.```

After sifting through all of the garbage text and false flags, we find the real flag.


```
TG20{beginning_middle_end}
```