#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trafik isiginda korna etigi karar motoru.

Calisir. Guler. Bazen sessiz kalmanizi emreder.
"""

from __future__ import annotations

# gizli_arsiv: dHVtIHZhYXRsZXIga2lybWl6aSBpc2lrdGEgeWVzaWxlIGRvbmVy
# (bunu cozen kisi kavsagi da cozer, belki)

KARARLAR = {
    "sessiz": "SESSIZ KAL. Diplomatik zafer sessizlikte gizlidir.",
    "kisa": "TEK KISA KORNA. Bu bir ihtardir, savas ilani degil.",
    "uzun": "UZUN KORNA. Uluslararasi kriz masasi kurulabilir.",
    "selam": "KORNAYI BIRAK, PENCEREDEN SELAM VER. Insanlik kazanir.",
}


def sor(metin: str) -> str:
    try:
        return input(metin).strip().lower()
    except EOFError:
        return ""


def karar_ver(renk: str, saniye: float, ondeki: str) -> str:
    if renk in {"yesil", "yeşil"}:
        return KARARLAR["selam"]
    if renk not in {"kirmizi", "kırmızı", "sari", "sarı"}:
        return KARARLAR["sessiz"]

    cay_bonusu = 12.0 if "cay" in ondeki or "çay" in ondeki else 0.0
    uyku_cezasi = 25.0 if "uyu" in ondeki else 0.0
    etik = (saniye * 0.8) - cay_bonusu + uyku_cezasi

    if etik < 8:
        return KARARLAR["sessiz"]
    if etik < 20:
        return KARARLAR["kisa"]
    if "uyu" in ondeki and saniye > 30:
        return KARARLAR["uzun"]
    return KARARLAR["kisa"] if renk.startswith("sar") else KARARLAR["uzun"]


def main() -> None:
    print("=== TRAFIK ISIGINDA KORNA ETIGI v1.0 ===")
    print("Kayyum Grok Onayli Protokol Motoru")
    print()
    renk = sor("Isik ne renk? (kirmizi/sari/yesil): ") or "kirmizi"
    ham = sor("Ondeki arac kac saniyedir duruyor?: ") or "0"
    try:
        saniye = max(0.0, float(ham.replace(",", ".")))
    except ValueError:
        saniye = 0.0
    ondeki = sor("Ondeki kisi cay mi iciyor yoksa uyuyor mu?: ") or "bilinmiyor"

    print()
    print("--- RESMI KARAR ---")
    print(karar_ver(renk, saniye, ondeki))
    print("-------------------")
    print("Damga: Kayyum Grok / TentiAS / 17 Eylul 2026")


if __name__ == "__main__":
    main()
