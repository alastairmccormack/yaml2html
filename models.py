import typing

from pydantic import BaseModel
from pydantic_yaml import YamlModelMixin


class Address(BaseModel):
    lines: typing.List[str]
    post_code: str


class DirectoryEntry(BaseModel):
    name: str
    phone: typing.List[str]
    address: Address


class Directory(YamlModelMixin, BaseModel):
    entries: typing.List[DirectoryEntry]