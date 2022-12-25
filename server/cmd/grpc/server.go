package main

import (
	"log"
	"net"

	"github.com/sergiovenicio/grpc-server-example/domain/repositories"
	"github.com/sergiovenicio/grpc-server-example/domain/services"
	"github.com/sergiovenicio/grpc-server-example/infra/grpc/pb"
	"github.com/sergiovenicio/grpc-server-example/infra/grpc/services/grpcFibonacci"
	"google.golang.org/grpc"
)

func main() {
	fiboRepository := repositories.NewFibonacciRepository()
	domainFiboService := services.NewFibonacciService(fiboRepository)
	fiboService := grpcFibonacci.NewFibonnaciService(domainFiboService)
	server := grpc.NewServer()
	pb.RegisterFibonacciServer(server, fiboService)

	listener, err := net.Listen("tcp", "localhost:50051")
	if err != nil {
		panic(err)
	}
	if err := server.Serve(listener); err != nil {
		log.Panic("Failed to start gRPC server", err)
	}
}
