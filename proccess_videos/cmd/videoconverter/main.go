package main

import (
	"log"
	"os"
	"videoprocess/internal/converter"
)

func main() {

	path := "/app/mediatest/media/uploads/1"

	if err := os.MkdirAll(path, os.ModePerm); err != nil {
		log.Fatalf("Erro ao criar diretório: %v", err)
	}

	vc := converter.NewVideoConverter()
	vc.Handle([]byte(`{"video_id": 1, "path": "` + path + `"}`))
}
