<?php 

error_reporting(E_ALL);
ini_set('display_errors', TRUE);
ini_set('display_startup_errors', TRUE);

if (!isset($_SERVER["HTTP_HOST"])) {
  parse_str($argv[1], $_GET);
  parse_str($argv[1], $_POST);
}

// Define o nome dos Lock Files
$lockVentilador = 'ventAUTO.txt';
$lockFogger = 'foggAUTO.txt';
$lockPainel = 'painelAUTO.txt';
$lockFotoperiodo = 'fotopAUTO.txt';
$lockIrriga = 'irrigaAUTO.txt';

// Define o nome dos scripts Files
$ventON = 'vent_ON.py';
$ventOFF = 'vent_OFF.py';
$foggON = 'fogg_ON.py';
$foggOFF = 'fogg_OFF.py';
$painelON = 'painel_ON.py';
$painelOFF = 'painel_OFF.py';
$fotopON = 'fotop_ON.py';
$fotopOFF = 'fotop_OFF.py';
$irrigaON = 'irriga_ON.py';
$irrigaOFF = 'irriga_OFF.py';
$linha1ON = 'linha1_ON.py';
$linha1OFF = 'linha1_OFF.py';
$linha2ON = 'linha2_ON.py';
$linha2OFF = 'linha2_OFF.py';
$linha3ON = 'linha3_ON.py';
$linha3OFF = 'linha3_OFF.py';
$linha4ON = 'linha4_ON.py';
$linha4OFF = 'linha4_OFF.py';
$bombaON = 'bomba_ON.py';
$bombaOFF = 'bomba_OFF.py';

// Pega a ação que veio do GET
$acao = $_GET['acao'];

//Define o caminho Base
$caminho = 'python /var/www/html/atuadores/';

//Verifica qual a ação que foi requisitada pelo aplicativo


/***************************************************
***                 VENTILADOR                   ***
****************************************************/

// Forçar Ligar Ventilador
if ($acao == 'ventON'){
	//$command = escapeshellcmd($caminho . $ventON );
	//$output = shell_exec($command);
	$output = system($caminho . $ventON, $retval);
	echo 'Retorno: ' . $retval . 	'</br>';
	if (file_exists ( $lockVentilador )){
		unlink($lockVentilador);		// Apaga o arquivo para "tirar do automático"
	}
	echo 'ventON';
}
// Forçar Desligamento do Ventilador
if ($acao =='ventOFF'){
	//$command = escapeshellcmd($caminho . $ventOFF);
	//$output = shell_exec($command);
	$output = system($caminho . $ventOFF, $retval);
	echo 'Retorno:' . $retval . 	'</br>';
	if (file_exists ( $lockVentilador )){
		unlink($lockVentilador);		// Apaga o arquivo para "tirar do automático"
	}
	echo 'ventOFF';
}
//Deixar que o Automático decida
if ($acao =='ventAUTO'){
	$file = fopen($lockVentilador, 'a');
	fwrite($file, 'ventAUTO');	//Cria o arquivo que determina o modo Automático
	fclose($file);
	$output = 'ventAUTO';
	echo $output;
}


/***************************************************
***                   FOGGER                     ***
****************************************************/

// Forçar Ligar Fogger
if ($acao == 'foggON'){
	echo $caminho . $foggON;
	$output = system($caminho . $foggON, $retval);
	echo 'Retorno: ' . $retval . '</br>';
	if (file_exists ( $lockFogger )){
		unlink($lockFogger);		// Apaga o arquivo para "tirar do automático"
	}
	echo 'foggON';
}
// Forçar Desligamento do Ventilador
if ($acao == 'foggOFF'){
	$output = system($caminho . $foggOFF, $retval);
	echo 'Retorno:' . $retval . '</br>';
	if (file_exists ( $lockFogger )){
		unlink($lockFogger);		// Apaga o arquivo para "tirar do automático"
	}
	echo 'foggOFF';
}
//Deixar que o Automático decida
if ($acao == 'foggAUTO'){
	$file = fopen($lockFogger, 'a');
	fwrite($file, 'foggAUTO');	//Cria o arquivo que determina o modo Automático
	fclose($file);
	$output = 'foggAUTO';
	echo $output;
}

/***************************************************
***                   FOTOPERIODO                ***
****************************************************/

// Forçar Ligar Iluminação
if ($acao == 'fotopON'){
	$output = system($caminho . $fotopON, $retval);
	echo 'Retorno: ' . $retval . '</br>';
	if (file_exists ( $lockFotoperiodo )){
		unlink($lockFotoperiodo);		// Apaga o arquivo para "tirar do automático"
	}
	echo 'fotopON';
}
// Forçar Desligamento da Iluminação
if ($acao == 'fotopOFF'){
	$output = system($caminho . $fotopOFF, $retval);
	echo 'Retorno:' . $retval . '</br>';
	if (file_exists ( $lockFotoperiodo )){
		unlink($lockFotoperiodo);		// Apaga o arquivo para "tirar do automático"
	}
	echo 'fotopOFF';
}
//Deixar que o Automático decida
if ($acao == 'fotopAUTO'){
	$file = fopen($lockFotoperiodo, 'a');
	fwrite($file, 'fotopAUTO');	//Cria o arquivo que determina o modo Automático
	fclose($file);
	$output = 'fotopAUTO';
	echo $output;
}

/***************************************************
***                 PAINEL UMIDO                 ***
****************************************************/

// Forçar Ligar Painel Humido
if ($acao == 'painelON'){
	$output = system($caminho . $painelON, $retval);
	echo 'Retorno: ' . $retval . 	'</br>';
	if (file_exists ( $lockPainel )){
		unlink($lockPainel);		// Apaga o arquivo para "tirar do automático"
	}
	echo 'painelON';
}
// Forçar Desligamento do Painel Umido
if ($acao =='painelOFF'){
	$output = system($caminho . $painelOFF, $retval);
	echo 'Retorno:' . $retval . 	'</br>';
	if (file_exists ( $lockPainel )){
		unlink($lockPainel);		// Apaga o arquivo para "tirar do automático"
	}
	echo 'painelOFF';
}
//Deixar que o Automático decida
if ($acao =='painelAUTO'){
	$file = fopen($lockPainel, 'a');
	fwrite($file, 'painelAUTO');	//Cria o arquivo que determina o modo Automático
	fclose($file);
	$output = 'painelAUTO';
	echo $output;
}

/***************************************************
***                 IRRIGAÇÃO	                 ***
****************************************************/

// Forçar Ligar Irrigação
if ($acao == 'irrigaON'){
	$output = system($caminho . $irrigaON, $retval);
	echo 'Retorno: ' . $retval . 	'</br>';
	if (file_exists ( $lockIrriga )){
		unlink($lockIrriga);		// Apaga o arquivo para "tirar do automático"
	}
	echo 'irrigaON';
}
// Forçar Desligamento da Irrigação
if ($acao =='irrigaOFF'){
	$output = system($caminho . $irrigaOFF, $retval);
	echo 'Retorno:' . $retval . 	'</br>';
	if (file_exists ( $lockIrriga )){
		unlink($lockIrriga);		// Apaga o arquivo para "tirar do automático"
	}
	echo 'irrigaOFF';
}
//Deixar que o Automático decida
if ($acao =='irrigaAUTO'){
	$file = fopen($lockIrriga, 'a');
	fwrite($file, 'irrigaAUTO');	//Cria o arquivo que determina o modo Automático
	fclose($file);
	$output = 'irrigaAUTO';
	echo $output;
}

/***************************************************
***                 LINHA 1 	                 ***
****************************************************/

// Ligar linha 1 Estufa 1
if ($acao == 'linha1ON'){
	$output = system($caminho . $linha1ON, $retval);
	echo 'Retorno: ' . $retval . 	'</br>';
	echo 'linha1ON';
}
// Forçar Desligamento da Irrigação
if ($acao =='linha1OFF'){
	$output = system($caminho . $linha1OFF, $retval);
	echo 'Retorno:' . $retval . 	'</br>';
	echo 'linha1OFF';
}

/***************************************************
***                 LINHA 2 	                 ***
****************************************************/

// Ligar linha 2 Estufa 1
if ($acao == 'linha2ON'){
	$output = system($caminho . $linha2ON, $retval);
	echo 'Retorno: ' . $retval . 	'</br>';
	echo 'linha2ON';
}
// Forçar Desligamento da Irrigação
if ($acao =='linha2OFF'){
	$output = system($caminho . $linha2OFF, $retval);
	echo 'Retorno:' . $retval . 	'</br>';
	echo 'linha2OFF';
}

/***************************************************
***                 LINHA 3 	                 ***
****************************************************/

// Ligar linha 3 Estufa 1
if ($acao == 'linha3ON'){
	$output = system($caminho . $linha3ON, $retval);
	echo 'Retorno: ' . $retval . 	'</br>';
	echo 'linha3ON';
}
// Forçar Desligamento da Irrigação
if ($acao =='linha3OFF'){
	$output = system($caminho . $linha3OFF, $retval);
	echo 'Retorno:' . $retval . 	'</br>';
	echo 'linha3OFF';
}

/***************************************************
***                 LINHA 4 	                 ***
***************************************************/

// Ligar linha 4 Estufa 1
if ($acao == 'linha4ON'){
	$output = system($caminho . $linha4ON, $retval);
	echo 'Retorno: ' . $retval . 	'</br>';
	echo 'linha4ON';
}
// Forçar Desligamento da Irrigação
if ($acao =='linha4OFF'){
	$output = system($caminho . $linha4OFF, $retval);
	echo 'Retorno:' . $retval . 	'</br>';
	echo 'linha4OFF';
}

/***************************************************
***                  BOMBA  	                 ***
****************************************************/

// Ligar Bomba Estufa 1
if ($acao == 'bombaON'){
	$output = system($caminho . $bombaON, $retval);
	echo 'Retorno: ' . $retval . 	'</br>';
	echo 'bombaON';
}
// Desligar Bomba Estufa 1
if ($acao =='bombaOFF'){
	$output = system($caminho . $bombaOFF, $retval);
	echo 'Retorno:' . $retval . 	'</br>';
	echo 'bombaOFF';
}
?>
