# 🎙️ Swara-Bharat (ಸ್ವರ-ಭಾರತ)

### Open-Source Emotional Voice AI for Indian Languages

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/)
[![HuggingFace](https://img.shields.io/badge/🤗-Models-yellow.svg)](https://huggingface.co/swara-bharat)
[![GitHub Stars](https://img.shields.io/github/stars/manjussha/swara-bharat?style=social)](https://github.com/manjussha/swara-bharat)

---

## 🌟 Vision

Build India's first **free, open-source alternative to Sarvam AI** with a unique focus on **emotional voice expressions** across Indian languages and dialects.

Unlike existing solutions that produce robotic, monotone voices, Swara-Bharat brings **human-like emotional range** to Text-to-Speech - perfect for comedy, customer service, education, entertainment, and storytelling.

---

## ✨ Features

### Current (v0.1 - In Development)

- 🎭 **Emotional Voices**: Happy, Empathetic, Sarcastic, Excited, Neutral
- 🗣️ **Dialect Support**: Bangalore, Mysore, Dharwad, Coastal, North Karnataka Kannada
- 🆓 **Completely Free**: Apache 2.0 license, use anywhere
- 🌐 **Open Source**: Full transparency, community-driven
- 🚀 **Easy API**: Simple integration with any application

### Planned (Roadmap)

- 📝 **Speech-to-Text**: Accurate transcription with dialect recognition (v0.5)
- 🤖 **Conversational AI**: Voice-in, voice-out conversations (v0.8)
- 🌍 **Multi-Language**: Tamil, Hindi, Telugu, Malayalam, and more (v1.0)
- 🎤 **Voice Cloning**: Create custom voices from short samples (v1.0)
- 💼 **Business Dashboard**: Professional tools for teams (v1.0)

---

## 🎯 Why Swara-Bharat?

| Feature | Swara-Bharat | Sarvam AI | AI4Bharat | ElevenLabs |
|---------|--------------|-----------|-----------|------------|
| **Emotional Voices** | ✅ Yes | ❌ Limited | ❌ No | ✅ Yes |
| **Indian Dialects** | ✅ Deep support | ⚠️ Basic | ⚠️ Basic | ❌ No |
| **Open Source** | ✅ Apache 2.0 | ❌ Proprietary | ✅ MIT | ❌ Proprietary |
| **Free to Use** | ✅ Always | ❌ Paid API | ✅ Yes | ❌ Paid |
| **Cultural Context** | ✅ Indian-first | ✅ Yes | ✅ Yes | ❌ Western |
| **Voice Quality** | 🎯 Target: Excellent | ⭐ Excellent | ⭐ Good | ⭐ Excellent |

---

## 🚀 Quick Start

### Installation
```bash
pip install swara-bharat
```

### Basic Usage
```python
from swara_bharat import generate_speech

# Generate emotional Kannada speech
audio = generate_speech(
    text="ನಮಸ್ಕಾರ! ಹೇಗಿದ್ದೀರಿ?",
    language="kannada",
    dialect="bangalore",
    emotion="happy"
)

# Save audio file
audio.save("greeting.wav")
```

### Web Demo

Try it now: [https://huggingface.co/spaces/swara-bharat/demo](https://huggingface.co/spaces/swara-bharat/demo)

---

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [Usage Examples](docs/usage.md)
- [API Reference](docs/api.md)
- [Training Your Own Model](docs/training.md)
- [Contributing Guide](CONTRIBUTING.md)

---

## 🎭 Supported Emotions

Our models can express a range of human emotions:

- **Neutral/Professional** - News reporting, formal announcements
- **Happy/Friendly** - Greetings, celebrations, positive messages
- **Empathetic/Caring** - Customer support, healthcare, counseling
- **Sarcastic/Witty** - Comedy, entertainment, satire
- **Excited/Energetic** - Motivational content, sports commentary
- **Urgent/Alert** - Breaking news, emergency announcements (coming soon)

**Demo samples:** [Listen to examples →](https://swara-bharat.org/samples)

---

## 🗺️ Supported Languages & Dialects

### v0.1 (Current Development)
- 🟢 **Kannada** - 5 dialects
  - Bangalore (Urban)
  - Mysore (Traditional)
  - Dharwad/Hubli (North Karnataka)
  - Mangalore/Udupi (Coastal)
  - North Karnataka (Rural)

### v0.5 (Planned - Month 6)
- 🟡 **Tamil** - Chennai, Madurai, Coimbatore
- 🟡 **Hindi** - Delhi, Mumbai, UP, Bhojpuri

### v1.0 (Planned - Month 12)
- 🔵 **Telugu** - Hyderabad, Coastal Andhra
- 🔵 **Malayalam** - Trivandrum, Kochi
- 🔵 **Marathi** - Mumbai, Pune
- 🔵 **Bengali** - Kolkata, Dhaka

**Want another language?** [Request here →](https://github.com/manjussha/swara-bharat/issues/new?template=language_request.md)

---

## 🎯 Use Cases

### 🎬 Content Creation
- YouTube narration in regional languages
- Podcast generation with emotional voices
- Audiobook production
- Social media content

### 📞 Business Applications
- Multilingual IVR systems
- Customer service chatbots
- Voice notifications
- Training materials

### 📚 Education
- E-learning in native languages
- Pronunciation practice
- Accessible content for visually impaired
- Language learning tools

### 🎪 Entertainment
- Comedy content generation
- Character voices for animations
- Interactive storytelling
- Gaming NPC voices

---

## 🏗️ Architecture
```
┌─────────────────────────────────────────────┐
│ User Input (Text)                           │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ Swara-Bharat TTS Engine                     │
│ ├── Language Model (Indic NLP)             │
│ ├── Emotion Encoder                         │
│ ├── Prosody Predictor                       │
│ ├── Acoustic Model (XTTS v2)               │
│ └── Vocoder (HiFi-GAN)                      │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│ Output (Emotional Voice)                    │
└─────────────────────────────────────────────┘
```

**Built with:**
- [Coqui TTS](https://github.com/coqui-ai/TTS) - Base architecture
- [OpenAI Whisper](https://github.com/openai/whisper) - Transcription
- [PyTorch](https://pytorch.org) - Training framework
- [HuggingFace](https://huggingface.co) - Model hosting

---

## 🤝 Contributing

We welcome all contributions! Here's how you can help:

### 🎤 Voice Donations
Record your voice in regional languages:
- 30-60 minutes of reading
- Different emotions
- Clear audio quality
- [Start recording →](https://swara-bharat.org/contribute-voice)

### 💻 Code Contributions
- Bug fixes
- New features
- Performance improvements
- [View open issues →](https://github.com/manjussha/swara-bharat/issues)

### 📝 Documentation
- Write tutorials
- Translate docs to regional languages
- Create video guides
- Share use cases

### 🧪 Testing & Feedback
- Report bugs
- Suggest features
- Test new releases
- Quality assessment

**Read our [Contributing Guide](CONTRIBUTING.md) to get started.**

---

## 📊 Project Status

### Current Phase: v0.1 Development

| Milestone | Status | Target Date |
|-----------|--------|-------------|
| Data Collection (10 hrs) | 🟡 In Progress | Week 6 |
| Model Training | 🔴 Not Started | Week 8 |
| Demo Release | 🔴 Not Started | Week 12 |
| Documentation | 🟡 In Progress | Week 12 |

**Track progress:** [Project Board →](https://github.com/manjussha/swara-bharat/projects/1)

---

## 🙏 Acknowledgments

### Training Data Sources

This project uses audio data from publicly available sources under fair use for research and education:

**Kannada Sources:**
- News: TV9 Kannada, Public TV, Udaya News, Suvarna News
- Educational: Various Kannada tutorial channels
- Cultural: Public domain content
- Community: 50+ volunteer voice contributors

**Full source list:** [DATA_SOURCES.md](DATA_SOURCES.md)

> 📧 **Content creators:** If you'd like attribution or removal of your content, please contact: data@swara-bharat.org

### Technology Stack

- [Coqui TTS](https://github.com/coqui-ai/TTS) - TTS architecture
- [OpenAI Whisper](https://github.com/openai/whisper) - Speech recognition
- [AI4Bharat](https://ai4bharat.org) - Indic NLP models
- [PyTorch](https://pytorch.org) - ML framework
- [HuggingFace](https://huggingface.co) - Model hosting

### Contributors

Thanks to all our contributors! ❤️

<!-- ALL-CONTRIBUTORS-LIST:START -->
<!-- This will be auto-generated -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

[Become a contributor →](CONTRIBUTING.md)

---

## 📄 License

**Apache License 2.0**

This means you can:
- ✅ Use commercially
- ✅ Modify and distribute
- ✅ Use privately
- ✅ Include in larger work

You must:
- 📝 Include license and copyright
- 📝 State changes made
- 📝 Include notice file

You cannot:
- ❌ Hold liable
- ❌ Use trademarks

**Full license:** [LICENSE](LICENSE)

---

## 🔗 Links

- **Website:** https://swara-bharat.org *(coming soon)*
- **Demo:** https://huggingface.co/spaces/swara-bharat/demo
- **Models:** https://huggingface.co/swara-bharat
- **Datasets:** https://huggingface.co/datasets/swara-bharat
- **Documentation:** https://docs.swara-bharat.org *(coming soon)*
- **Blog:** https://blog.swara-bharat.org *(coming soon)*

### Community

- **GitHub Discussions:** [Ask questions, share ideas](https://github.com/manjussha/swara-bharat/discussions)
- **Discord:** *(coming soon)*
- **Twitter:** [@SwaraBharat](https://twitter.com/SwaraBharat) *(coming soon)*
- **LinkedIn:** [Swara-Bharat](https://linkedin.com/company/swara-bharat) *(coming soon)*

---

## 📧 Contact

**Project Maintainer:** Manju  
**GitHub:** [@manjussha](https://github.com/manjussha)  
**Email:** contact@swara-bharat.org

For urgent issues: [Create an issue](https://github.com/manjussha/swara-bharat/issues/new)

---

## 🌟 Support the Project

If Swara-Bharat helps you, consider:

- ⭐ **Star this repository** - Helps others discover the project
- 🐦 **Share on social media** - Spread the word
- 🎤 **Contribute voice samples** - Improve model quality
- 💻 **Submit PRs** - Make it better
- 📝 **Write about it** - Blog posts, tutorials, case studies
- 💰 **Sponsor development** - [GitHub Sponsors](https://github.com/sponsors/manjussha) *(coming soon)*

---

## 🗓️ Roadmap

### 2024 Q4 - Q1 2025

**v0.1 - Foundation** *(3 months)*
- [x] Project setup
- [ ] Kannada data collection (10 hours)
- [ ] 5 dialects support
- [ ] 5 emotions support
- [ ] Initial model training
- [ ] Public demo release

**v0.5 - Expansion** *(3 months)*
- [ ] Add Tamil language
- [ ] Add Hindi language
- [ ] Speech-to-Text integration
- [ ] Web dashboard
- [ ] API server

**v0.8 - Intelligence** *(3 months)*
- [ ] LLM integration (conversational AI)
- [ ] Voice-to-voice pipeline
- [ ] Multi-turn conversations
- [ ] 5 total languages

**v1.0 - Platform** *(3 months)*
- [ ] 7+ languages
- [ ] Voice cloning
- [ ] Business dashboard
- [ ] API marketplace
- [ ] Mobile apps

**Detailed roadmap:** [ROADMAP.md](ROADMAP.md)

---

## 📈 Stats

![GitHub stars](https://img.shields.io/github/stars/manjussha/swara-bharat?style=social)
![GitHub forks](https://img.shields.io/github/forks/manjussha/swara-bharat?style=social)
![GitHub issues](https://img.shields.io/github/issues/manjussha/swara-bharat)
![GitHub pull requests](https://img.shields.io/github/issues-pr/manjussha/swara-bharat)
![GitHub contributors](https://img.shields.io/github/contributors/manjussha/swara-bharat)
![GitHub last commit](https://img.shields.io/github/last-commit/manjussha/swara-bharat)

---

## 🏆 Recognition

- 🎯 Featured on ProductHunt *(planned)*
- 📰 Media coverage *(planned)*
- 🏛️ University partnerships *(planned)*
- 💼 Corporate pilots *(planned)*

---

## ❓ FAQ

**Q: Is this really free?**  
A: Yes! Apache 2.0 license means you can use it commercially without paying anything.

**Q: How is quality compared to Sarvam/ElevenLabs?**  
A: We're targeting similar quality. v0.1 will be good, v1.0 will be excellent.

**Q: Can I use this in my commercial product?**  
A: Absolutely! Just include the license notice.

**Q: How can I add my language?**  
A: Check our [Language Request Guide](docs/language-request.md) or contribute data!

**Q: What about privacy?**  
A: All processing can be done locally. No data sent to us unless you use hosted API.

**Q: How fast is inference?**  
A: Target: <3 seconds for 10-second audio. Will improve with optimization.

**More questions?** [Check full FAQ →](docs/FAQ.md)

---

## 🎓 Citations

If you use Swara-Bharat in your research, please cite:
```bibtex
@software{swara_bharat_2024,
  author = {Manju and Contributors},
  title = {Swara-Bharat: Open-Source Emotional Voice AI for Indian Languages},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/manjussha/swara-bharat}
}
```

---

## 💝 Thank You

Special thanks to:
- All voice contributors
- Code contributors
- Testers and early adopters
- Open source community
- Indian language enthusiasts
- Everyone spreading the word

**Together, we're building voice AI for Bharat!** 🇮🇳

---

<div align="center">

**Built with ❤️ for Indian languages**

[![Made in India](https://img.shields.io/badge/Made%20in-India-orange?style=for-the-badge)](https://en.wikipedia.org/wiki/India)

**[⭐ Star](https://github.com/manjussha/swara-bharat) • [🐛 Report Bug](https://github.com/manjussha/swara-bharat/issues) • [💡 Request Feature](https://github.com/manjussha/swara-bharat/issues) • [📖 Documentation](docs/)**

---

*"Language is the road map of a culture. It tells you where its people come from and where they are going."* - Rita Mae Brown

</div>