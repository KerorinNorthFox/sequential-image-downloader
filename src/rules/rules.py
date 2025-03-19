from rules.rule import Rule
from rules.eromanga_life_com_rule import EromangaLifeComRule
from rules.moeero_library_com_rule import MoeeroLibraryComRule
from rules.eromanga_cafe_com_rule import EromangaCafeComRule
from rules.eroproject_com_rule import EroprojectComRule
from rules.jsiro_to_rule import JsiroToRule
from rules.momon_ga_com_rule import MomonGaComRule
from rules.ddd_smart_net_rule import DDDSmartNetRule
from rules.ita_do_com_rule import ItaDoComRule
from rules.www_mangalear_blog_rule import WWWMangalearBlogRule
from rules.nukibooks_com_rule import NukibooksComRule
from rules.nyahentai_re_rule import NyahentaiReRule
from rules.jcomic_net_rule import JcomicNetRule
from rules.eromanga_kiwami_com_rule import EromangaKiwamiComRule
from rules.himebon_blog_rule import HimebonBlogRule
from rules.nijigen_daiaru_com_rule import NijigenDaiaruComRule
from rules.eromanga_celeb_com_rule import EromangaCelebComRule
from rules.erodoujinshi_world_com_rule import ErodoujinshiWorldComRule
from rules.com_hokan_site_rule import ComHokanSiteRule
from rules.oreno_erohon_com_rule import OrenoErohonComRule
from rules.hentai_books_com_rule import HentaiBooksComRule
from rules.web_archive_org_rule import WebArchiveOrgRule
from rules.book18_fans_rule import Book18FansRule
from rules.www_sexloveero_net_rule import WWWSexloveeroNetRule
from rules.javdeep_net_rule import JavDeepNetRule

RULES: list[Rule] = [
    EromangaLifeComRule(),
    MoeeroLibraryComRule(),
    EromangaCafeComRule(),
    EroprojectComRule(),
    JsiroToRule(),
    MomonGaComRule(),
    DDDSmartNetRule(),
    ItaDoComRule(),
    WWWMangalearBlogRule(),
    NukibooksComRule(),
    NyahentaiReRule(),
    JcomicNetRule(),
    EromangaKiwamiComRule(),
    HimebonBlogRule(),
    NijigenDaiaruComRule(),
    EromangaCelebComRule(),
    ErodoujinshiWorldComRule(),
    ComHokanSiteRule(),
    OrenoErohonComRule(),
    HentaiBooksComRule(),
    WebArchiveOrgRule(),
    Book18FansRule(),
    WWWSexloveeroNetRule(),
    JavDeepNetRule(),
]