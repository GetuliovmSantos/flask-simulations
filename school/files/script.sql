-- Esquema: school-flask
DROP SCHEMA IF EXISTS `school-flask`;

-- Criação do esquema: school-flask
CREATE SCHEMA IF NOT EXISTS `school-flask` DEFAULT CHARACTER SET utf8;
USE `school-flask`;

-- Tabela: usuarios
CREATE TABLE IF NOT EXISTS `school-flask`.`usuarios` (
  `loginUsuario` VARCHAR(10) NOT NULL,
  `nomeUsuario` VARCHAR(45) NOT NULL,
  `senhaUsuario` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`loginUsuario`))
ENGINE = InnoDB;

-- Tabela: turmas
CREATE TABLE IF NOT EXISTS `school-flask`.`turmas` (
  `codTurma` INT NOT NULL AUTO_INCREMENT,
  `nomeTurma` VARCHAR(45) NOT NULL,
  `periodoTurma` CHAR(1) NOT NULL,
  `loginUsuario` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`codTurma`),
  FOREIGN KEY (`loginUsuario`)
    REFERENCES `school-flask`.`usuarios` (`loginUsuario`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- Tabela: atividades
CREATE TABLE IF NOT EXISTS `school-flask`.`atividades` (
  `idAtividade` INT NOT NULL AUTO_INCREMENT,
  `nomeAtividade` VARCHAR(45) NOT NULL,
  `descricaoAtividade` VARCHAR(45) NOT NULL,
  `dataAtividade` DATE NOT NULL,
  `pesoAtividade` INT NOT NULL,
  `codTurma` INT NOT NULL,
  PRIMARY KEY (`idAtividade`),
  FOREIGN KEY (`codTurma`)
    REFERENCES `school-flask`.`turmas` (`codTurma`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;