# 2021-02-15 10:08:46 -03
- Started learning golang, compiles pretty quick
- Watching some hacking streams
  - https://www.twitch.tv/hackingesports
  - appears to be related to this tournament: https://www.ctf.live/
- Got some useful links
  - https://tryhackme.com/ - for hacking challenges
  - https://mermaid-js.github.io/mermaid/#/ - diagrams as code, useful for mindmaps, sequence diagrams, gantt, etc
- Had a meeting about terraform wrappers
  - https://github.com/tlopo-ruby/tfw
  - https://terragrunt.gruntwork.io/
  - https://git.mckinsey-solutions.com/Martin-Kelly/scaffold

# 2021-02-16 10:01:56 -03
- Q# (Q Sharp) is a language used for Quantum Computing
- [crazy4pi314](https://www.twitch.tv/crazy4pi314/) streams quantum computing on twitch

# 2021-02-22 09:47:55 -03
- the study-notes really helped me remember what I was studying after having to take a break from study for a week due to work

# 2021-02-24 10:11:13 -03
- Azure has its own CloudFormation/Terraform kinda functionality in AzureResourceManager(ARM), and they really try to push powershell adoption for managing azure (but it is not required)
- After struggling a little bit with helm templates, trying to escape the dollar sign '$' from a configmap used to build a nginx.conf file, I found the problem actually was an envsubst being executed in the deployment pipeline, that is why I was able to install the helm chart locally, but it kept breaking when executed through the pipeline, should've realized it sooner
- .Files.Get is broken on Helm v2.8.2 (dont known when it was fixed)
