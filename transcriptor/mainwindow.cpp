#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    auto font = QFont("Noto Sans", 12);
    ui->input->setFont(font);
    ui->output->setFont(font);

    connect(ui->input, SIGNAL(textChanged()), this, SLOT(translate()));
}

struct TranslationPair {
    QString in;
    QString out;
};

const TranslationPair pairs[] {
    { "tsh", "ћ" },
    { "TSH", "Ћ" },
    { "dzh", "ђ" },
    { "DZH", "Ђ" },
    { "ng", "ӈ" },
    { "NG", "Ӈ" },
    { "ts", "ц" },
    { "TS", "Ц" },
    { "dz", "ѕ" },
    { "DZ", "Ѕ" },
    { "sh", "ш" },
    { "SH", "Ш" },
    { "zh", "ж" },
    { "ZH", "Ж" },
    { "m", "м" },
    { "M", "М" },
    { "p", "п" },
    { "P", "П" },
    { "b", "б" },
    { "B", "Б" },
    { "f", "ф" },
    { "F", "Ф" },
    { "v", "в" },
    { "V", "В" },
    { "n", "н" },
    { "N", "Н" },
    { "t", "т" },
    { "T", "Т" },
    { "d", "д" },
    { "D", "Д" },
    { "s", "с" },
    { "S", "С" },
    { "z", "з" },
    { "Z", "З" },
    { "l", "л" },
    { "L", "Л" },
    { "k", "к" },
    { "K", "К" },
    { "g", "г" },
    { "G", "Г" },
    { "h", "х" },
    { "H", "Х" },
    { "i", "и" },
    { "I", "И" },
    { "e", "е" },
    { "E", "Е" },
    { "a", "а" },
    { "A", "А" },
    { "o", "о" },
    { "O", "О" },
    { "u", "у" },
    { "U", "У" },
    { "y", "й" },
    { "Y", "Й" },
    { "w", "ў" },
    { "W", "Ў" },
    { "q", "ь" },
    { "Q", "Ь" },
    { "r", "л" },
    { "R", "Л" },
    { "j", "й" },
    { "J", "Й" },
    { "x", "х" },
    { "X", "Х" },
    { "c", "с" },
    { "C", "С" },
};

void MainWindow::translate() {
    auto text = ui->input->toPlainText();
    for (auto &p: pairs) {
        text = text.replace(p.in, p.out);
    }
    ui->output->setText(text);
}

MainWindow::~MainWindow()
{
    delete ui;
}

