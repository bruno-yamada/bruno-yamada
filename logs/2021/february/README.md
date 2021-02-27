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

# 2021-02-25 16:44:25 -03
- I should learn more advanced `POSIX shell` and `perl`
- Docker Swarm focus on spinning up containers at scale, k8s is about distributed system lifecycle
- Today I found out that gitleaks(v7.2.2) failed to discover several fairly in-your-face secrets within a repo, luckly it was before it being made public, it probably works well at detecting asymmetric private keys, but by itself, it is not enough to tell that a repo does not contains any exposed secrets

# 2021-02-27 09:31:00 -03
- after being through many jobs and contracts, I can say now with confidence, that at the beginning things might seem overwheling and complicated, but after about 3 months, you had enough time to get the whole picture and work through many cases, and then, you know most things
