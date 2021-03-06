# YAMl 
based on [v1.2 spec](https://yaml.org/spec/1.2/spec.html)

> “YAML Ain’t Markup Language” (abbreviated YAML) is a data serialization language designed to be human-friendly and work well with modern programming languages for common everyday tasks.

## YAML Goals (in order of priority)
- __YAML is easily readable by humans.__
- YAML data is portable between programming languages.
- YAML matches the native data structures of agile languages.
- YAML has a consistent model to support generic tools.
- YAML supports one-pass processing.
- YAML is expressive and extensible.
- YAML is easy to implement and use.

So YAML takes easy-to-read as its first priority

# Details
- Borrows and inspired by known standards and technologies: Internet Mail (RFC0822), MIME (RFC2045)
  - indented like python
  - double-quote scaping like C
  - end-of-line like HTML (line breaks are folded into single line, blank line into line-break, allowing word-wrap for visility)
  - types are inspired by perl, python and ruby
    - supporting colletions, sequences and scalars for easily being transported into those language's data types
  - alias and rich data structures like SOAP
  - TODO > YAML was designed to support incremental interfaces that include both input (“getNextEvent()”) and output (“sendNextEvent()”) one-pass interfaces. Together, these enable YAML to support the processing of large documents (e.g. transaction logs) or continuous streams (e.g. feeds from a production machine).
- regarding JSON
  - both tries to give more readability
  - JSON aims first at simplicity and universality, YAML focus at readability at the cost of being more complex to generate and parse
  - JSON keys SHOULB be unique (duplicates replace one another) while YAML keys MUST be unique (otherwise raising an error)
- regarding XML
  - YAML is primarily a data serialization language. XML was designed to be backwards compatible with the Standard Generalized Markup Language (SGML)
  - There is an ongoing effort to define YAML/XML mappings, more details at [http://yaml.org/xml](http://yaml.org/xml.)

Single example doc:
```yaml
```

