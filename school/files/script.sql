-- Esquema: school-flask
DROP SCHEMA IF EXISTS `school-flask`;

-- Criação do esquema: school-flask
CREATE SCHEMA IF NOT EXISTS `school-flask` DEFAULT CHARACTER SET utf8;
USE `school-flask`;

-- Tabela: usuarios
CREATE TABLE IF NOT EXISTS `school-flask`.`usuarios` (
  `loginUsuario` INT NOT NULL,
  `nomeUsuario` VARCHAR(45) NOT NULL,
  `senhaUsuario` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`loginUsuario`))
ENGINE = InnoDB;

-- Tabela: turmas
CREATE TABLE IF NOT EXISTS `school-flask`.`turmas` (
  `codTurma` INT NOT NULL AUTO_INCREMENT,
  `nomeTruma` VARCHAR(45) NULL,
  `periodo` CHAR(1) NULL,
  `turmascol` VARCHAR(45) NULL,
  `loginUsuario` INT NOT NULL,
  PRIMARY KEY (`codTurma`),
  FOREIGN KEY (`loginUsuario`)
    REFERENCES `school-flask`.`usuarios` (`loginUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- Tabela: atividades
CREATE TABLE IF NOT EXISTS `school-flask`.`atividades` (
  `idAtividades` INT NOT NULL,
  `nomeAtividade` VARCHAR(45) NOT NULL,
  `descricaoAtividade` VARCHAR(45) NOT NULL,
  `dataAtividade` DATE NOT NULL,
  `pesoAtividade` INT NOT NULL,
  `codTurma` INT NOT NULL,
  PRIMARY KEY (`idAtividades`),
  FOREIGN KEY (`codTurma`)
    REFERENCES `school-flask`.`turmas` (`codTurma`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
