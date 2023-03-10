sample_snap = {
    "name": "test_snap_data",
    "snap": {
        "media": [
            {
                "height": 512,
                "type": "icon",
                "url": "https://randomurl.com/icon.png",
                "width": 512,
            },
            {
                "height": 1365,
                "type": "banner",
                "url": "https://randomurl.com/banner.png",
                "width": 4095,
            },
            {
                "height": 1000,
                "type": "screenshot",
                "url": "https://randomurl.com/screenshot.png",
                "width": 1500,
            },
            {
                "height": 1000,
                "type": "screenshot",
                "url": "https://randomurl.com/screenshot.png",
                "width": 1500,
            },
            {
                "height": 1000,
                "type": "screenshot",
                "url": "https://randomurl.com/screenshot.png",
                "width": 1500,
            },
            {
                "height": 1000,
                "type": "screenshot",
                "url": "https://randomurl.com/screenshot.png",
                "width": 1500,
            },
            {
                "height": 1000,
                "type": "screenshot",
                "url": "https://randomurl.com/screenshot.png",
                "width": 1500,
            },
        ],
        "publisher": {
            "display-name": "Publisher Name",
            "id": "randompublisherID",
            "username": "publisher_name",
            "validation": "unproven",
        },
        "summary": "snap data",
        "title": "Test snap data",
        "categories": [{"name": "category name", "slug": "category-slug"}],
    },
    "snap-id": "somerandomID",
}

sample_charm = {
    "default-release": {
        "channel": {
            "base": {
                "architecture": "all",
                "channel": "20.04",
                "name": "ubuntu",
            },
            "name": "stable",
            "released-at": "released-at",
            "risk": "stable",
            "track": "latest",
        },
        "revision": {"revision": 123},
    },
    "id": "someID",
    "name": "A charm name",
    "result": {
        "categories": [
            {
                "featured": False,
                "name": "category name",
                "slug": "category-slug",
            }
        ],
        "deployable-on": [],
        "media": [
            {
                "height": "",
                "type": "icon",
                "url": "https://randomurl.com/icon.png",
                "width": "",
            }
        ],
        "publisher": {"display-name": "Publisher name"},
        "summary": "A charm summary",
        "title": "",
    },
    "type": "charm",
    "store_front": {
        "icons": ["https://randomurl.com/icon.png"],
        "deployable-on": [""],
        "categories": [
            {"featured": False, "name": "Databases", "slug": "databases"}
        ],
        "display-name": "Postgresql",
    },
}

sample_package_list = [
    {
        "package": {"name": "test1"},
        "publisher": {"display-name": "publisher test1"},
        "categories": [{"name": "cat-1", "display_name": "cat 1"}],
        "platforms": ["VM", "kubernetes"],
        "package_type": "charm",
    },
    {
        "package": {"name": "test2"},
        "publisher": {"display-name": "publisher test2"},
        "categories": [{"name": "cat-2", "display_name": "cat 2"}],
        "platforms": ["VM"],
        "package_type": "charm",
    },
    {
        "package": {"name": "test9"},
        "publisher": {"display-name": "publisher test9"},
        "categories": [{"name": "cat-2", "display_name": "cat 2"}],
        "platforms": ["VM"],
        "package_type": "charm",
    },
    {
        "package": {"name": "test14"},
        "publisher": {"display-name": "publisher test14"},
        "categories": [{"name": "cat-1", "display_name": "cat 1"}],
        "platforms": ["kubernetes"],
        "package_type": "charm",
    },
    {
        "package": {"name": "test11"},
        "publisher": {"display-name": "publisher test11"},
        "categories": [{"name": "cat-3", "display_name": "test cat 3"}],
        "platforms": ["kubernetes"],
        "package_type": "charm",
    },
    {
        "package": {"name": "test3"},
        "publisher": {"display-name": "publisher test3"},
        "categories": [{"name": "cat-3", "display_name": "cat 3"}],
        "platforms": ["VM"],
        "package_type": "bundle",
    },
    {
        "package": {"name": "test4"},
        "publisher": {"display-name": "publisher test4"},
        "categories": [{"name": "cat-3", "display_name": "cat 3"}],
        "platforms": ["kubernetes"],
        "package_type": "bundle",
    },
    {
        "package": {"name": "test10"},
        "publisher": {"display-name": "publisher test10"},
        "categories": [{"name": "cat-3", "display_name": "test cat 3"}],
        "platforms": ["kubernetes", "VM"],
        "package_type": "bundle",
    },
    {
        "package": {"name": "test12"},
        "publisher": {"display-name": "publisher test12"},
        "categories": [{"name": "cat-3", "display_name": "test cat 12"}],
        "platforms": ["VM"],
        "package_type": "bundle",
    },
    {
        "package": {"name": "test13"},
        "publisher": {"display-name": "publisher test13"},
        "categories": [{"name": "cat-1", "display_name": "cat 1"}],
        "platforms": ["VM"],
        "package_type": "bundle",
    },
]

sample_package_list2 = [
    {
        "package": {"name": "test15"},
        "publisher": {"display-name": "publisher test15"},
        "categories": [{"name": "cat-1", "display_name": "cat 1"}],
        "platforms": ["arch3"],
        "package_type": "snap",
    },
    {
        "package": {"name": "test5"},
        "publisher": {"display-name": "publisher test5"},
        "categories": [{"name": "cat-3", "display_name": "cat 3"}],
        "platforms": ["arch1"],
        "package_type": "snap",
    },
    {
        "package": {"name": "test6"},
        "publisher": {"display-name": "publisher test6"},
        "categories": [{"name": "cat-2", "display_name": "cat 2"}],
        "platforms": ["arch1"],
        "package_type": "snap",
    },
    {
        "package": {"name": "test7"},
        "publisher": {"display-name": "publisher test7"},
        "categories": [{"name": "cat-2", "display_name": "cat 2"}],
        "platforms": ["arch1", "arch2"],
        "package_type": "snap",
    },
    {
        "package": {"name": "test8"},
        "publisher": {"display-name": "publisher test8"},
        "categories": [{"name": "cat-2", "display_name": "cat 2"}],
        "platforms": ["arch2"],
        "package_type": "snap",
    },
]
