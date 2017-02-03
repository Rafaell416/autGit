package main

import (
 "fmt"
 "log"
 "os/exec"

)

func main() {
	/*
	leer Comentario
	*/
leerComentario()    

}

func leerComentario() {
	//var comentario string
	//fmt.Println("Comentario: ")
    //fmt.Scanf("%s",&comentario)
    //fmt.Println("hola",comentario)
    //cmd := exec.Command("/bin/sh", mongoToCsvSH)
     out, err := exec.Command("if netcat -z google.com 80; then echo “Tienes conexion”; else echo “no tienes conexion”; fi").Output()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("The  %s\n", out)

 
}