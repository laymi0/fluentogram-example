from fluent_compiler.bundle import FluentBundle

from fluentogram import FluentTranslator, TranslatorHub


def create_translator_hub() -> TranslatorHub:
    translator_hub = TranslatorHub(
        {
            "ru": ("ru", "en", "uz"),
            "en": ("en", "ru", "uz"),
            "uz": ("uz", "en", "ru")
        },
        [
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale="ru-RU",
                    filenames=["locales/ru/LC_MESSAGES/txt.ftl"])),
            FluentTranslator(
                locale="en",
                translator=FluentBundle.from_files(
                    locale="en-US",
                    filenames=["locales/en/LC_MESSAGES/txt.ftl"])),
            FluentTranslator(
                locale="uz",
                translator=FluentBundle.from_files(
                    locale="uz-UZ",
                    filenames=["locales/uz/LC_MESSAGES/txt.ftl"]))
        ],
    )
    return translator_hub