from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import (
    BaseSiteSetting,
    register_setting,
)


class BuildablePage(Page):
    body = StreamField(
        [
            (
                "section",
                blocks.StructBlock(
                    [
                        (
                            "add_container",
                            blocks.BooleanBlock(default=True, required=False),
                        ),
                        (
                            "add_vertical_padding",
                            blocks.BooleanBlock(default=True, required=False),
                        ),
                        (
                            "children",
                            blocks.StreamBlock(
                                [
                                    (
                                        "images",
                                        blocks.StructBlock(
                                            [
                                                (
                                                    "n_column_filled",
                                                    blocks.IntegerBlock(default=12),
                                                ),
                                                (
                                                    "images",
                                                    blocks.StreamBlock(
                                                        [
                                                            (
                                                                "image",
                                                                ImageChooserBlock(
                                                                    required=True
                                                                ),
                                                            ),
                                                        ]
                                                    ),
                                                ),
                                            ]
                                        ),
                                    ),
                                    (
                                        "rich_text",
                                        blocks.StructBlock(
                                            [
                                                (
                                                    "n_column_filled",
                                                    blocks.IntegerBlock(default=12),
                                                ),
                                                ("rich_text", blocks.RichTextBlock()),
                                            ]
                                        ),
                                    ),
                                    (
                                        "contact_form",
                                        blocks.StructBlock(
                                            [
                                                (
                                                    "n_column_filled",
                                                    blocks.IntegerBlock(default=12),
                                                ),
                                            ]
                                        ),
                                    ),
                                    (
                                        "latest_articles",
                                        blocks.StructBlock(
                                            [
                                                (
                                                    "n_column_filled",
                                                    blocks.IntegerBlock(default=12),
                                                ),
                                                (
                                                    "number_of_articles",
                                                    blocks.IntegerBlock(default=3),
                                                ),
                                                (
                                                    "style",
                                                    blocks.ChoiceBlock(
                                                        choices=[
                                                            ("list", "List"),
                                                            (
                                                                "horizontal_scrolling_cards",
                                                                "Horizontal Scrolling Cards",
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ]
                                        ),
                                    ),
                                ]
                            ),
                        ),
                    ]
                ),
            )
        ]
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


@register_setting
class LogoSettings(BaseSiteSetting):
    logo_for_light_background = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    logo_for_dark_background = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )


@register_setting
class EmailSettings(BaseSiteSetting):
    email_host = models.CharField(max_length=255)
    email_port = models.IntegerField()
    email_host_user = models.CharField(max_length=255)
    email_host_password = models.CharField(max_length=255)
    email_use_tls = models.BooleanField(default=False)
    email_use_ssl = models.BooleanField(default=False)


@register_setting
class ContactSettings(BaseSiteSetting):
    send_email_to_admin = models.BooleanField(default=True)
    email_subject_for_admin = models.CharField(
        max_length=255,
    )
    email_content_for_admin = models.TextField(
        help_text="Available variables: {first_name}, {last_name}, {phone_number}, {email}, {details}",
    )
    admin_recipient_email = models.EmailField()
    send_email_to_visitor = models.BooleanField(default=True)
    email_subject_for_visitor = models.CharField(
        max_length=255,
    )
    email_content_for_visitor = models.TextField(
        help_text="available_variables: {first_name}, {last_name}",
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("send_email_to_admin"),
                FieldPanel("email_subject_for_admin"),
                FieldPanel("email_content_for_admin"),
                FieldPanel("admin_recipient_email"),
            ],
            heading="Email settings for admin",
        ),
        MultiFieldPanel(
            [
                FieldPanel("send_email_to_visitor"),
                FieldPanel("email_subject_for_visitor"),
                FieldPanel("email_content_for_visitor"),
            ],
            heading="Email settings for visitor",
        ),
    ]


@register_setting
class NavigationSettings(BaseSiteSetting):
    header_navigation_links = StreamField(
        [
            (
                "page_link",
                blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock()),
                        ("page", blocks.PageChooserBlock()),
                        (
                            "open_in_new_tab",
                            blocks.BooleanBlock(default=False, required=False),
                        ),
                    ]
                ),
            ),
            (
                "external_link",
                blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock()),
                        ("url", blocks.URLBlock()),
                        (
                            "open_in_new_tab",
                            blocks.BooleanBlock(default=False, required=False),
                        ),
                    ]
                ),
            ),
        ]
    )
    footer_navigation_links = StreamField(
        [
            (
                "page_link",
                blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock()),
                        ("page", blocks.PageChooserBlock()),
                        (
                            "open_in_new_tab",
                            blocks.BooleanBlock(default=False, required=False),
                        ),
                    ]
                ),
            ),
            (
                "external_link",
                blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock()),
                        ("url", blocks.URLBlock()),
                        (
                            "open_in_new_tab",
                            blocks.BooleanBlock(default=False, required=False),
                        ),
                    ]
                ),
            ),
        ]
    )
