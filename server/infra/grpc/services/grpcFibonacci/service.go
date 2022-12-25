package grpcFibonacci

import (
	"context"

	"github.com/google/uuid"

	"github.com/sergiovenicio/grpc-server-example/domain/entities"
	domainServices "github.com/sergiovenicio/grpc-server-example/domain/services"
	"github.com/sergiovenicio/grpc-server-example/infra/grpc/pb"
)

type FibonnaciGRPCService struct {
	domainService *domainServices.FibonacciService
	pb.UnimplementedFibonacciServer
}

func (s *FibonnaciGRPCService) GetFibonacci(ctx context.Context, in *pb.GetRequest) (*pb.GetResponse, error) {
	request, err := s.domainService.Find(in.ProcessId)
	if err != nil {
		return nil, err
	}

	return &pb.GetResponse{
		Status: request.Status,
		Result: request.Result,
	}, nil
}

func (s *FibonnaciGRPCService) CalcFibonacci(ctx context.Context, in *pb.CalcRequest) (*pb.CalcResponse, error) {
	id, _ := uuid.NewUUID()
	request := entities.CalcRequest{
		Id:     id.String(),
		Number: in.Number,
		Status: "REQUESTED",
	}
	s.domainService.Register(&request)

	go s.domainService.Calc(&request)

	return &pb.CalcResponse{
		ProcessId: request.Id,
		Status:    request.Status,
	}, nil
}

func NewFibonnaciService(service *domainServices.FibonacciService) *FibonnaciGRPCService {
	return &FibonnaciGRPCService{
		domainService: service,
	}
}
