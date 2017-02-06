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
     out, err := exec.Command("echo 'hola'").Output()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf( out)

 
}