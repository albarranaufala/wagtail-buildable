from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel


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
